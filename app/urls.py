from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, reverse

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts', views.contacts, name='contact'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
