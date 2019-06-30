import pika
from json import dumps, loads
import random


QUEUE_IMAGES = 'images'
QUEUE_RESULT = 'result'


connection = None
channel_send = None
channel_receive = None

db = dict()


def _prepare():
    """
    Prepare pika connection
    """
    global connection
    global channel_send
    global channel_receive

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

    channel_send = connection.channel()
    channel_send.queue_declare(queue=QUEUE_IMAGES)

    channel_receive = connection.channel()
    channel_receive.queue_declare(queue=QUEUE_RESULT)


def send_to_ml(id: int, path: str):
    """
    Send request to ML for file processing
    """
    global channel_send

    _prepare()
    channel_send.basic_publish(
            exchange='',
            routing_key=QUEUE_IMAGES,
            body=dumps({'id': id, 'path': path})
    )


def receive_from_ml(id: int) -> str or None:
    """
    Check if file is already processed by ML
    :returns: None if no result is available
    """
    global db
    global channel_receive

    if id in db:
        return db[id]

    _prepare()

    while True:
        print("receive_from_ml check")
        ok, prop, body = channel_receive.basic_get(queue=QUEUE_RESULT, auto_ack=True)
        if ok is None:
            break

        r = loads(body)
        db[int(r['id'])] = r['path']
        print("receive_from_ml {} at {}".format(r['id'], r['path']))

    print(db)
    print("ID is {}".format(id))
    return db.get(int(id))

# Attractive
# Caring
# Aggressive
# Intelligent
# Confident
# Emotionally stable
# Trustworthy
# Responsible
# Unhappy
# Dominant

def get_ml_data(image):
    random.seed(27)

    attractive = random.randint(0,9)
    caring = random.randint(0,9)
    aggressive = random.randint(0,9)
    intelligent = random.randint(0,9)
    confident = random.randint(0,9)
    emotionally_stable = random.randint(0,9)
    trustworthy = random.randint(0,9)
    responsible = random.randint(0,9)
    unhappy = random.randint(0,9)
    dominant = random.randint(0,9)

    dict = {}

    dict["attractive"] = attractive
    dict["caring"] = caring
    dict["aggressive"] = aggressive
    dict["intelligent"] = intelligent
    dict["confident"] = confident
    dict["emotionally_stable"] = emotionally_stable
    dict["trustworthy"] = trustworthy
    dict["responsible"] = responsible
    dict["unhappy"] = unhappy
    dict["dominant"] = dominant

    return dict
