from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView

from rest_framework.decorators import api_view

from .api import upload, result

from rest_framework.status import HTTP_404_NOT_FOUND


class IndexView(TemplateView):
    template_name = 'index.html'


@api_view(['POST'])
def user_upload(request):
    """
    Upload view for the user.
    """
    answer = upload(request)
    if len(answer) == 4:
        login = answer[0] 
        password = answer[1]
        image = answer[2]
        test = answer[3]
        data = result(login, password, image, test)
        return JsonResponse(data, safe=False)
    else:
        return HttpResponse(status=400)
