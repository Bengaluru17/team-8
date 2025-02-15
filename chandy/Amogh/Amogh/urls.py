"""Amogh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from db.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

uploader_instance = Uploader()
restful_instance = RestfulEndpoints()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', uploader_instance.index),
    url(r'^find/', uploader_instance.upload),
    url(r'^login/', uploader_instance.return_login),
    url(r'^login-validate/', uploader_instance.validate_auth),
    url(r'^logout/', uploader_instance.logout),
    url(r'^form-new/', uploader_instance.make_form),
    url(r'^form-submit/', uploader_instance.VALIDATE_form),
    url(r'^form-show/', uploader_instance.show_data),
    url(r'^form-submit-url/', uploader_instance.submit_url),
    url(r'^api/inc/', restful_instance.inc_points),

]


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', serve, {
            'document_root': settings.STATIC_ROOT,
        }),
    ]
