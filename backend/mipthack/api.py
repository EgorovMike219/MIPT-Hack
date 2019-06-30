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
# 'CMake': 5, 'Java': 9, 'Yacc': 6, 'Lex': 5, 'Ruby': 5, 'PowerShell': 3, 'TeX': 9, 'C#': 8, 'API Blueprint':  'Makefile': 5, 'Perl 6': 4, 'Handlebars': 4, 'PHP': 1}

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

    data1.append([0, 0, react_native, "React Native"])
    data1.append([0, 1, swift, "Swift"])
    data1.append([0, 2, winapi, "Win Api"])
    data1.append([0, 3, cpp, "C++"])
    data1.append([0, 4, c_sharp, "C#"])
    data1.append([0, 5, java, "Java"])
    data1.append([0, 6, python, "Python"])
    data1.append([0, 7, qt, "Qt"])
    data1.append([0, 8, go, "Go"])
    data1.append([0, 9, electron, "Electron"])

    sum_data1 = react_native + swift + winapi + cpp + c_sharp + java + python + qt + go + electron

    data2.append([1, 0, test[0] * 2, "Leadership"])
    data2.append([1, 1, test[0] * 2, "Management"])
    data2.append([1, 2, test[1] * 2, "Problem Solving"])
    data2.append([1, 3, test[1] * 2, "Decision Making"])
    data2.append([1, 4, test[2] * 2, "Listening"])
    data2.append([1, 5, test[2] * 2, "Speaking"])
    data2.append([1, 6, test[3] * 2, "Self-Confidence"])
    data2.append([1, 7, test[3] * 2, "Positive-thinking"])
    data2.append([1, 8, test[4] * 2, "Prioritisation"])
    data2.append([1, 9, test[4] * 2, "Scheduling"])

    sum_data2 = sum(test) * 2

    data3.append([2, 0, python, "Python"])
    data3.append([2, 1, r, "R"])
    data3.append([2, 2, cpp, "C++"])
    data3.append([2, 3, scala, "Scala"])
    data3.append([2, 4, swift, "Swift"])
    data3.append([2, 5, jupyter_notebook, "Jupyter Notebook"])
    data3.append([2, 6, tensorflow, "TensorFlow"])
    data3.append([2, 7, mathematics, "Mathematics"])
    data3.append([2, 8, pytorch, "PyTorch"])
    data3.append([2, 9, keras, "Keras"])

    sum_data3 = python + r + cpp + scala + swift + jupyter_notebook + tensorflow + mathematics + pytorch + keras

    data4.append([3, 0, js, "JavaScript"])
    data4.append([3, 1, css, "CSS"])
    data4.append([3, 2, html, "HTML"])
    data4.append([3, 3, jquery, "JQuery"])
    data4.append([3, 4, reactjs, "ReactJS"])
    data4.append([3, 5, angular, "Angular"])
    data4.append([3, 6, typescript, "TypeScript"])
    data4.append([3, 7, vuejs, "VueJS"])
    data4.append([3, 8, bootstrap, "Bootstrap"])
    data4.append([3, 9, restapi, "REST API"])

    sum_data4 = js + css + html + jquery + reactjs + angular + typescript + vuejs + bootstrap + restapi

    data5.append([4, 0, python, "Python"])
    data5.append([4, 1, java, "Java"])
    data5.append([4, 2, c, "C"])
    data5.append([4, 3, cpp, "C++"])
    data5.append([4, 4, c_sharp, "C#"])
    data5.append([4, 5, php, "PHP"])
    data5.append([4, 6, ruby, "Ruby"])
    data5.append([4, 7, sql, "SQL"])
    data5.append([4, 8, cmake, "CMake"])
    data5.append([4, 9, djangofreim, "Django"])

    sum_data5 = python + java + c + cpp + c_sharp + php + ruby + sql + cmake + djangofreim

    data6.append([5, 0, python, "Python"])
    data6.append([5, 1, shell, "Shell"])
    data6.append([5, 2, perl, "Perl"])
    data6.append([5, 3, cpp, "C++"])
    data6.append([5, 4, c, "C"])
    data6.append([5, 5, linux, "Linux"])
    data6.append([5, 6, protocols, "Protocols"])
    data6.append([5, 7, winapi, "Win Api"])
    data6.append([5, 8, apach, "Apach"])
    data6.append([5, 9, nginx, "Nginx"])

    sum_data6 = python + shell + perl + cpp + c + linux + protocols + winapi + apach + nginx

    data7.append([6, 0, swift, "Swift"])
    data7.append([6, 1, java, "Java"])
    data7.append([6, 2, kotlin, "Kotlin"])
    data7.append([6, 3, objectivec, "Objective-C"])
    data7.append([6, 4, mobile_angular, "Mobile Angular UI"])
    data7.append([6, 5, react_native, "React Native"])
    data7.append([6, 6, xamarin, "Xamarin"])
    data7.append([6, 7, flutter, "Flutter"])
    data7.append([6, 8, apach, "Apach"])
    data7.append([6, 9, ionic, "Ionic"])

    sum_data7 = swift + java + kotlin + objectivec + mobile_angular + react_native + xamarin + flutter + apach + ionic

    data8.append([7, 0, c_sharp, "C#"])
    data8.append([7, 1, cpp, "C++"])
    data8.append([7, 2, opengl, "OpenGL"])
    data8.append([7, 3, cuda, "CUDA"])
    data8.append([7, 4, unity, "Unity"])
    data8.append([7, 5, unreal_engine, "Unreal Engine"])
    data8.append([7, 6, augmented_knowledge, "Augmented Knowledge"])
    data8.append([7, 7, modeling3d, "3D modeling"])
    data8.append([7, 8, audio_knowledge, "Audio Knowledge"])
    data8.append([7, 9, vr, "Virtual Reality"])

    sum_data8 = c_sharp + cpp + opengl + cuda + unity + unreal_engine + augmented_knowledge + modeling3d + audio_knowledge + vr

    data9.append([8, 0, python, "Python"])
    data9.append([8, 1, cpp, "C++"])
    data9.append([8, 2, java, "Java"])
    data9.append([8, 3, c, "C"])
    data9.append([8, 4, go, "Go"])
    data9.append([8, 5, c_sharp, "C#"])
    data9.append([8, 6, php, "PHP"])
    data9.append([8, 7, unit_test, "Unit test"])
    data9.append([8, 8, google_test, "Google test"])
    data9.append([8, 9, test_knowledge, "Test Knowledge"])

    sum_data9 = python + cpp + java + c + go + c_sharp + php + unit_test + google_test + test_knowledge

    data10.append([9, 0, ml_data[0], "Attractive"])
    data10.append([9, 1, ml_data[1], "Caring"])
    data10.append([9, 2, ml_data[2], "Aggressive"])
    data10.append([9, 3, ml_data[3], "Intelligent"])
    data10.append([9, 4, ml_data[4], "Confident"])
    data10.append([9, 5, ml_data[5], "Emotionally stable"])
    data10.append([9, 6, ml_data[6], "Trustworthy"])
    data10.append([9, 7, ml_data[7], "Responsible"])
    data10.append([9, 8, ml_data[8], "Unhappy"])
    data10.append([9, 9, ml_data[9], "Dominant"])
    sum_data10 = sum(ml_data)

    sum_data = [[sum_data1, 1], [sum_data2, 2], [sum_data3, 3], [sum_data4, 4], [sum_data5,5], [sum_data6,6], [sum_data7,7], [sum_data8,8], [sum_data9,9], [sum_data10,10]]

    data1.sort(key=lambda x: x[2], reverse=True)
    data2.sort(key=lambda x: x[2], reverse=True)
    data3.sort(key=lambda x: x[2], reverse=True)
    data4.sort(key=lambda x: x[2], reverse=True)
    data5.sort(key=lambda x: x[2], reverse=True)
    data6.sort(key=lambda x: x[2], reverse=True)
    data7.sort(key=lambda x: x[2], reverse=True)
    data8.sort(key=lambda x: x[2], reverse=True)
    data9.sort(key=lambda x: x[2], reverse=True)
    data10.sort(key=lambda x: x[2], reverse=True)

    data = []

    sum_data.sort(key=lambda x: x[0], reverse=True)

    for i in sum_data:
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

    print(data)

    return data








