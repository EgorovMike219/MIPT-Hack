"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views import generic
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from .views.auth import *
from django.conf import settings
from django.conf.urls.static import static
from django.core.exceptions import PermissionDenied
from django.conf.urls.static import static

from rest_framework.decorators import api_view
from django.http import JsonResponse

from populate.views import *

@api_view(['GET'])
def perform_test(request):
    ret = {'test': 2, 'fds': 3}
    return JsonResponse(ret)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', generic.RedirectView.as_view(url='/api/', permanent=False)),
    path('api/', get_schema_view(title="API Monitoring")),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/notes/', include('notes.urls')),
    path('api/testing/', perform_test),
    path('api/auth/register/', Registration.as_view()),
    # path('api/tags/', include('tags.urls')),

    # path('populate/users/<int:total>', populate_users),
    # path('populate/notes/<int:total>', populate_notes),
    # path('populate/note_votes/<int:percent_likes>', populate_votes)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

