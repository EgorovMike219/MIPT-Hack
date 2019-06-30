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
from .get_keypoints import get_keypoints, transform_img_with_keypoints


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

#Output: {'JavaScript': 'Python': 'CSS': 'HTML': 'Assembly': 'C': 'C++': 'Shell': 'Jupyter Notebook':
# 'CMake': 'Java': 'Yacc': 'Lex': 'Ruby': 'PowerShell': 'TeX': 'C#': 'API Blueprint':  'Makefile': 'Perl 6': 'Handlebars': 'PHP': 1}

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
    return languages

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

def softmax10(arr):
    return 7 * (arr - np.min(arr)) / np.max(arr)

def get_ml_data(image):

    keypoints = get_keypoints(image)
    w = np.array(keypoints)
    data_keypoints = w[0]



    arr_for_softmax = np.array([np.mean(data_keypoints[:10,:,:]), np.mean(data_keypoints[10:20,:,:]), np.mean(data_keypoints[20:30,:,:]),
                       np.mean(data_keypoints[30:40,:,:]), np.mean(data_keypoints[40:50,:,:]), np.mean(data_keypoints[50:60,:,:]),
                       np.mean(data_keypoints[60:70,:,:]), np.mean(data_keypoints[70:80,:,:]), np.mean(data_keypoints[80:90,:,:]),
                       np.mean(data_keypoints[90:,:,:])]) * np.array(range(1, 11))

    data = list(np.array(softmax10(arr_for_softmax), dtype=int))
    data = [int(value) for value in data]
    print(data)

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
    #print(languages_data)
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
        jupyter_notebook = languages_data["Jupyter Notebook"]
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

    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    data6 = []
    data7 = []
    data8 = []
    data9 = []
    data10 = []

    data1.append(["Desktop", react_native, "React Native"])
    data1.append(["Desktop", swift, "Swift"])
    data1.append(["Desktop", winapi, "Win Api"])
    data1.append(["Desktop", cpp, "C++"])
    data1.append(["Desktop", c_sharp, "C#"])
    data1.append(["Desktop", java, "Java"])
    data1.append(["Desktop", python, "Python"])
    data1.append(["Desktop", qt, "Qt"])
    data1.append(["Desktop", go, "Go"])
    data1.append(["Desktop", electron, "Electron"])

    sum_data1 = react_native + swift + winapi + cpp + c_sharp + java + python + qt + go + electron

    data2.append(["Soft Skills", test[0] * 2, "Leadership"])
    data2.append(["Soft Skills", test[0] * 2, "Management"])
    data2.append(["Soft Skills", test[1] * 2, "Problem\n Solving"])
    data2.append(["Soft Skills", test[1] * 2, "Decision\n Making"])
    data2.append(["Soft Skills", test[2] * 2, "Listening"])
    data2.append(["Soft Skills", test[2] * 2, "Speaking"])
    data2.append(["Soft Skills", test[3] * 2, "Self-\nConfidence"])
    data2.append(["Soft Skills", test[3] * 2, "Positive-think"])
    data2.append(["Soft Skills", test[4] * 2, "Prioritisation"])
    data2.append(["Soft Skills", test[4] * 2, "Scheduling"])

    sum_data2 = sum(test) * 4

    data3.append(["ML", python, "Python"])
    data3.append(["ML", r, "R"])
    data3.append(["ML", cpp, "C++"])
    data3.append(["ML", scala, "Scala"])
    data3.append(["ML", swift, "Swift"])
    data3.append(["ML", jupyter_notebook, "Jupyter Noteb."])
    data3.append(["ML", tensorflow, "TensorFlow"])
    data3.append(["ML", mathematics, "Mathematics"])
    data3.append(["ML", pytorch, "PyTorch"])
    data3.append(["ML", keras, "Keras"])

    sum_data3 = python + r + cpp + scala + swift + jupyter_notebook + tensorflow + mathematics + pytorch + keras

    data4.append(["FrontEnd", js, "JavaScript"])
    data4.append(["FrontEnd", css, "CSS"])
    data4.append(["FrontEnd", html, "HTML"])
    data4.append(["FrontEnd", jquery, "JQuery"])
    data4.append(["FrontEnd", reactjs, "ReactJS"])
    data4.append(["FrontEnd", angular, "Angular"])
    data4.append(["FrontEnd", typescript, "TypeScript"])
    data4.append(["FrontEnd", vuejs, "VueJS"])
    data4.append(["FrontEnd", bootstrap, "Bootstrap"])
    data4.append(["FrontEnd", restapi, "REST API"])

    sum_data4 = js + css + html + jquery + reactjs + angular + typescript + vuejs + bootstrap + restapi

    data5.append(["BackEnd", python, "Python"])
    data5.append(["BackEnd", java, "Java"])
    data5.append(["BackEnd", c, "C"])
    data5.append(["BackEnd", cpp, "C++"])
    data5.append(["BackEnd", c_sharp, "C#"])
    data5.append(["BackEnd", php, "PHP"])
    data5.append(["BackEnd", ruby, "Ruby"])
    data5.append(["BackEnd", sql, "SQL"])
    data5.append(["BackEnd", cmake, "CMake"])
    data5.append(["BackEnd", djangofreim, "Django"])

    sum_data5 = python + java + c + cpp + c_sharp + php + ruby + sql + cmake + djangofreim

    data6.append(["DevOps", python, "Python"])
    data6.append(["DevOps", shell, "Shell"])
    data6.append(["DevOps", perl, "Perl"])
    data6.append(["DevOps", cpp, "C++"])
    data6.append(["DevOps", c, "C"])
    data6.append(["DevOps", linux, "Linux"])
    data6.append(["DevOps", protocols, "Protocols"])
    data6.append(["DevOps", winapi, "Win Api"])
    data6.append(["DevOps", apach, "Apach"])
    data6.append(["DevOps", nginx, "Nginx"])

    sum_data6 = python + shell + perl + cpp + c + linux + protocols + winapi + apach + nginx

    data7.append(["MobileDev", swift, "Swift"])
    data7.append(["MobileDev", java, "Java"])
    data7.append(["MobileDev", kotlin, "Kotlin"])
    data7.append(["MobileDev", objectivec, "Objective-C"])
    data7.append(["MobileDev", mobile_angular, "Mob.Angular UI"])
    data7.append(["MobileDev", react_native, "React Native"])
    data7.append(["MobileDev", xamarin, "Xamarin"])
    data7.append(["MobileDev", flutter, "Flutter"])
    data7.append(["MobileDev", apach, "Apach"])
    data7.append(["MobileDev", ionic, "Ionic"])

    sum_data7 = swift + java + kotlin + objectivec + mobile_angular + react_native + xamarin + flutter + apach + ionic

    data8.append(["GameDev", c_sharp, "C#"])
    data8.append(["GameDev", cpp, "C++"])
    data8.append(["GameDev", opengl, "OpenGL"])
    data8.append(["GameDev", cuda, "CUDA"])
    data8.append(["GameDev", unity, "Unity"])
    data8.append(["GameDev", unreal_engine, "Unreal\n Engine"])
    data8.append(["GameDev", augmented_knowledge, "Aug. Knowledge"])
    data8.append(["GameDev", modeling3d, "3D modeling"])
    data8.append(["GameDev", audio_knowledge, "Aud. Knowledge"])
    data8.append(["GameDev", vr, "Virtual Reality"])

    sum_data8 = c_sharp + cpp + opengl + cuda + unity + unreal_engine + augmented_knowledge + modeling3d + audio_knowledge + vr

    data9.append(["Test", python, "Python"])
    data9.append(["Test", cpp, "C++"])
    data9.append(["Test", java, "Java"])
    data9.append(["Test", c, "C"])
    data9.append(["Test", go, "Go"])
    data9.append(["Test", c_sharp, "C#"])
    data9.append(["Test", php, "PHP"])
    data9.append(["Test", unit_test, "Unit test"])
    data9.append(["Test", google_test, "Google\n test"])
    data9.append(["Test", test_knowledge, "Test\n Knowledge"])

    sum_data9 = python + cpp + java + c + go + c_sharp + php + unit_test + google_test + test_knowledge

    data10.append(["Personality", ml_data[0], "Attractive"])
    data10.append(["Personality", ml_data[1], "Caring"])
    data10.append(["Personality", ml_data[2], "Aggressive"])
    data10.append(["Personality", ml_data[3], "Intelligent"])
    data10.append(["Personality", ml_data[4], "Confident"])
    data10.append(["Personality", ml_data[5], "Emotion. stable"])
    data10.append(["Personality", ml_data[6], "Trustworthy"])
    data10.append(["Personality", ml_data[7], "Responsible"])
    data10.append(["Personality", ml_data[8], "Unhappy"])
    data10.append(["Personality", ml_data[9], "Dominant"])
    sum_data10 = sum(ml_data)

    sum_data = [[sum_data1, 1], [sum_data2, 2], [sum_data3, 3], [sum_data4, 4], [sum_data5,5], [sum_data6,6], [sum_data7,7], [sum_data8,8], [sum_data9,9], [sum_data10,10]]

    data1.sort(key=lambda x: x[1], reverse=True)
    data2.sort(key=lambda x: x[1], reverse=True)
    data3.sort(key=lambda x: x[1], reverse=True)
    data4.sort(key=lambda x: x[1], reverse=True)
    data5.sort(key=lambda x: x[1], reverse=True)
    data6.sort(key=lambda x: x[1], reverse=True)
    data7.sort(key=lambda x: x[1], reverse=True)
    data8.sort(key=lambda x: x[1], reverse=True)
    data9.sort(key=lambda x: x[1], reverse=True)
    data10.sort(key=lambda x: x[1], reverse=True)

    data = []

    sum_data.sort(key=lambda x: x[0], reverse=True)

    sum_data_copy = [[], [], [], [], [], [], [], [], [], []]

    sum_data_copy[4] = sum_data[0]
    sum_data_copy[5] = sum_data[1]
    sum_data_copy[3] = sum_data[2]
    sum_data_copy[6] = sum_data[3]
    sum_data_copy[2] = sum_data[4]
    sum_data_copy[7] = sum_data[5]
    sum_data_copy[1] = sum_data[6]
    sum_data_copy[8] = sum_data[7]
    sum_data_copy[0] = sum_data[8]
    sum_data_copy[9] = sum_data[9]

    for i in sum_data_copy:
        if i[1] == 1:
            for x in data1:
                data.append(x)
        elif i[1] == 2:
            for x in data2:
                data.append(x)
        elif i[1] == 3:
            for x in data3:
                data.append(x)
        elif i[1] == 4:
            for x in data4:
                data.append(x)
        elif i[1] == 5:
            for x in data5:
                data.append(x)
        elif i[1] == 6:
            for x in data6:
                data.append(x)
        elif i[1] == 7:
            for x in data7:
                data.append(x)
        elif i[1] == 8:
            for x in data8:
                data.append(x)
        elif i[1] == 9:
            for x in data9:
                data.append(x)
        elif i[1] == 10:
            for x in data10:
                data.append(x)

    ind = 0
    for x in range(1, 11):
        for y in range(1, 11):
           data[ind] += [x, y]
           ind += 1

    return data








