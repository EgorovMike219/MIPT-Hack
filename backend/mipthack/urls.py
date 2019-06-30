from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url

from .views import user_upload
from .views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^upload$', user_upload)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

