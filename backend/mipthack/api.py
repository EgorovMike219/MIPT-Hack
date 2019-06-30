from django.core.exceptions import ObjectDoesNotExist
from django.core.files.base import ContentFile

from rest_framework.response import Response
from rest_framework.status import \
    HTTP_400_BAD_REQUEST, \
    HTTP_404_NOT_FOUND

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializer import githubSerializer, pictureSerializer, testSerializer

from .models import Picture, Test, Github
from .api_ml import send_to_ml, receive_from_ml
from PIL import Image
import base64
import io
import numpy as np
import cv2
from github import Github
import random


def check(value):
    if value <= 100:
        return 0
    if value <= 250:
        return 1
    if value <= 500:
        return 2
    if value <= 1000:
        return 3
    if value <= 3000:
        return 4
    if value <= 10000:
        return 5
    if value <= 50000:
        return 6
    if value <= 150000:
        return 7
    if value <= 500000:
        return 8
    else:
        return 9

#Output: {'JavaScript': 9, 'Python': 8, 'CSS': 9, 'HTML': 9, 'Assembly': 4, 'C': 8, 'C++': 8, 'Shell': 5, 'Jupyter Notebook': 9,
# 'CMake': 5, 'Java': 9, 'Yacc': 6, 'Lex': 5, 'Ruby': 5, 'PowerShell': 3, 'TeX': 9, 'C#': 8, 'API Blueprint': 7, 'Makefile': 5, 'Perl 6': 4, 'Handlebars': 4, 'PHP': 1}

def get_languages_data(user, password):
    # using username and password
    g = Github(user, password)

    languages = {}

    # Then play with your Github objects:
    for repo in g.get_user().get_repos():
       lang_dict = repo.get_languages()
       lang = list(lang_dict.keys())
       for l in lang:
           if l in languages:
               languages[l] += lang_dict[l]
           else:
               languages[l] = lang_dict[l]

    languages = {key: check(value) for key, value in languages.items()}

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

    data = [attractive, caring, aggressive, intelligent,confident, emotionally_stable, trustworthy, responsible, unhappy, dominant]

    return data


# Take in base64 string and return cv image
def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    image = Image.open(io.BytesIO(imgdata))
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        login = data['login']
        password = data['password']
        img_data = data['picture']
        image = stringToRGB(img_data)
        cv2.imwrite('image.png',image)
        test = data['test']
        return [login, password, image, test]
    return [0]

def result(login, password, image, test):
    random.seed(27)
    languages_data = get_languages_data(login, password)
    ml_data = get_ml_data(image)

    if 'C++' in languages_data:
        cpp = languages_data['C++']
    else:
        cpp = random.randint(0,9)

    if 'JavaScript' in languages_data:
        js = languages_data['JavaScript']
    else:
        js = random.randint(0,9)

    if 'Python' in languages_data:
        python = languages_data['Python']
    else:
        python = random.randint(0,9)

    if 'CSS' in languages_data:
        css = languages_data['CSS']
    else:
        css = random.randint(0,9)

    if 'HTML' in languages_data:
        html = languages_data['HTML']
    else:
        html = random.randint(0,9)

    if 'C' in languages_data:
        c = languages_data['C']
    else:
        c = random.randint(0,9)

    if 'Jupyter Notebook' in languages_data:
        jupyter_notebook = languages_data['Jupyter Notebook']
    else:
        jupyter_notebook = random.randint(0,9)

    if 'R' in languages_data:
        r = languages_data['R']
    else:
        r = random.randint(0,9)

    if 'Scala' in languages_data:
        scala = languages_data['Scala']
    else:
        scala = random.randint(0,9)

    if 'Swift' in languages_data:
        swift = languages_data['Swift']
    else:
        swift = random.randint(0,9)

    if 'C#' in languages_data:
        c_sharp = languages_data['C#']
    else:
        c_sharp = random.randint(0,9)

    if 'Java' in languages_data:
        java = languages_data['Java']
    else:
        java = random.randint(0,9)

    if 'Go' in languages_data:
        go = languages_data['Go']
    else:
        go = random.randint(0,9)

    if 'PHP' in languages_data:
        php = languages_data['PHP']
    else:
        php = random.randint(0,9)

    if 'Ruby' in languages_data:
        ruby = languages_data['Ruby']
    else:
        ruby = random.randint(0,9)

    if 'SQL' in languages_data:
        sql = languages_data['SQL']
    else:
        sql = random.randint(0,9)

    if 'CMake' in languages_data:
        cmake = languages_data['CMake']
    else:
        cmake = random.randint(0,9)

    if 'Shell' in languages_data:
        shell = languages_data['Shell']
    else:
        shell = random.randint(0,9)

    if 'Perl 6' in languages_data:
        perl = languages_data['Perl 6']
    else:
        perl = random.randint(0,9)

    if 'Kotlin' in languages_data:
        kotlin = languages_data['Kotlin']
    else:
        kotlin = random.randint(0,9)

    if 'Objective-C' in languages_data:
        objectivec = languages_data['Objective-C']
    else:
        objectivec = random.randint(0,9)

    react_native = random.randint(0, 9)

    winapi = random.randint(0, 9)
    qt = random.randint(0, 9)
    electron = random.randint(0, 9)
    tensorflow = random.randint(0, 9)
    mathematics = random.randint(0, 9)
    pytorch = random.randint(0, 9)
    keras = random.randint(0, 9)
    jquery = random.randint(0, 9)
    reactjs = random.randint(0, 9)
    angular = random.randint(0, 9)
    typescript = random.randint(0, 9)
    vuejs = random.randint(0, 9)
    bootstrap = random.randint(0, 9)
    restapi = random.randint(0, 9)
    djangofreim = random.randint(0, 9)
    linux = random.randint(0, 9)
    protocols = random.randint(0, 9)
    apach = random.randint(0, 9)
    nginx = random.randint(0, 9)
    mobile_angular = random.randint(0, 9)
    xamarin = random.randint(0, 9)
    flutter = random.randint(0, 9)
    ionic = random.randint(0, 9)

    opengl = random.randint(0, 9)
    cuda = random.randint(0, 9)
    unity = random.randint(0, 9)
    unreal_engine = random.randint(0, 9)
    augmented_knowledge = random.randint(0, 9)
    modeling3d = random.randint(0, 9)
    audio_knowledge = random.randint(0, 9)
    vr = random.randint(0, 9)

    unit_test = random.randint(0, 9)
    google_test = random.randint(0, 9)
    test_knowledge = random.randint(0, 9)

    data = []
    types = ["Apps", "Soft Skills", "ML", "FrontEnd", "BackEnd", "DevOps", "MobileDev", "GameDev", "Test Master", "Physiognomy"]
    data.append([0, 0, react_native, "React Native"])

    data.append([0, 1, swift, "Swift"])
    data.append([0, 2,winapi, "Win Api"])
    data.append([0, 3,cpp, "C++"])
    data.append([0, 4,c_sharp,"C#"])
    data.append([0, 5,java,"Java"])
    data.append([0, 6,python,"Python"])
    data.append([0, 7,qt,"Qt"])
    data.append([0, 8,go,"Go"])
    data.append([0, 9,electron,"Electron"])

    data.append([1, 0,test[0],"Leadership"])
    data.append([1, 1,test[0],"Management"])
    data.append([1, 2,test[1],"Problem Solving"])
    data.append([1, 3,test[1],"Decision Making"])
    data.append([1, 4,test[2],"Listening"])
    data.append([1, 5,test[2],"Speaking"])
    data.append([1, 6,test[3],"Self-Confidence"])
    data.append([1, 7,test[3],"Positive-thinking"])
    data.append([1, 8,test[4],"Prioritisation"])
    data.append([1, 9,test[4],"Scheduling"])

    data.append([2, 0,python,"Python"])
    data.append([2, 1,r,"R"])
    data.append([2, 2,cpp,"C++"])
    data.append([2, 3,scala,"Scala"])
    data.append([2, 4,swift,"Swift"])
    data.append([2, 5,jupyter_notebook,"Jupyter Notebook"])
    data.append([2, 6,tensorflow, "TensorFlow"])
    data.append([2, 7,mathematics,"Mathematics"])
    data.append([2, 8,pytorch,"PyTorch"])
    data.append([2, 9,keras,"Keras"])

    data.append([3, 0,js,"JavaScript"])
    data.append([3, 1,css,"CSS"])
    data.append([3, 2,html,"HTML"])
    data.append([3, 3,jquery,"JQuery"])
    data.append([3, 4,reactjs,"ReactJS"])
    data.append([3, 5,angular,"Angular"])
    data.append([3, 6,typescript,"TypeScript"])
    data.append([3, 7,vuejs,"VueJS"])
    data.append([3, 8,bootstrap,"Bootstrap"])
    data.append([3, 9,restapi, "REST API"])

    data.append([4, 0,python,"Python"])
    data.append([4, 1,java,"Java"])
    data.append([4, 2,c,"C"])
    data.append([4, 3,cpp,"C++"])
    data.append([4, 4,c_sharp,"C#"])
    data.append([4, 5,php,"PHP"])
    data.append([4, 6,ruby,"Ruby"])
    data.append([4, 7,sql,"SQL"])
    data.append([4, 8,cmake,"CMake"])
    data.append([4, 9,djangofreim,"Django"])

    data.append([5, 0,python,"Python"])
    data.append([5, 1,shell,"Shell"])
    data.append([5, 2,perl,"Perl"])
    data.append([5, 3,cpp,"C++"])
    data.append([5, 4,c,"C"])
    data.append([5, 5,linux,"Linux"])
    data.append([5, 6,protocols,"Protocols"])
    data.append([5, 7,winapi,"Win Api"])
    data.append([5, 8,apach,"Apach"])
    data.append([5, 9,nginx,"Nginx"])

    data.append([6, 0,swift,"Swift"])
    data.append([6, 1,java,"Java"])
    data.append([6, 2,kotlin,"Kotlin"])
    data.append([6, 3,objectivec,"Objective-C"])
    data.append([6, 4,mobile_angular,"Mobile Angular UI"])
    data.append([6, 5,react_native,"React Native"])
    data.append([6, 6,xamarin,"Xamarin"])
    data.append([6, 7,flutter,"Flutter"])
    data.append([6, 8,apach,"Apach"])
    data.append([6, 9,ionic,"Ionic"])

    data.append([7, 0,c_sharp,"C#"])
    data.append([7, 1,cpp,"C++"])
    data.append([7, 2,opengl,"OpenGL"])
    data.append([7, 3,cuda,"CUDA"])
    data.append([7, 4,unity,"Unity"])
    data.append([7, 5,unreal_engine,"Unreal Engine"])
    data.append([7, 6,augmented_knowledge,"Augmented Knowledge"])
    data.append([7, 7,modeling3d,"3D modeling"])
    data.append([7, 8,audio_knowledge,"Audio Knowledge"])
    data.append([7, 9,vr,"Virtual Reality"])

    data.append([8, 0,python,"Python"])
    data.append([8, 1,cpp,"C++"])
    data.append([8, 2,java,"Java"])
    data.append([8, 3,c,"C"])
    data.append([8, 4,go,"Go"])
    data.append([8, 5,c_sharp,"C#"])
    data.append([8, 6,php,"PHP"])
    data.append([8, 7,unit_test,"Unit test"])
    data.append([8, 8,google_test,"Google test"])
    data.append([8, 9,test_knowledge,"Test Knowledge"])

    data.append([9, 0,ml_data[0],"Attractive"])
    data.append([9, 1,ml_data[1],"Caring"])
    data.append([9, 2,ml_data[2],"Aggressive"])
    data.append([9, 3,ml_data[3],"Intelligent"])
    data.append([9, 4,ml_data[4],"Confident"])
    data.append([9, 5,ml_data[5],"Emotionally stable"])
    data.append([9, 6,ml_data[6],"Trustworthy"])
    data.append([9, 7,ml_data[7],"Responsible"])
    data.append([9, 8,ml_data[8],"Unhappy"])
    data.append([9, 9,ml_data[9], "Dominant"])

    return data








