"""ContactBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from MyClass.views import*


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^new$', AddPerson.as_view()),
    url(r'^(?P<id>\d+)/addPhone$', AddPhone.as_view()),
    url(r'^(?P<id>\d+)/addAdress$', AddAdress.as_view()),
    url(r'^(?P<id>\d+)/addEmail$', AddEmail.as_view()),
    url(r'^addGroup$', AddGroup.as_view()),
    url(r'^modify/(?P<id>\d+)$', PersonEdit.as_view()),
    url(r'^modifyAdress/(?P<id>\d+)$', modifyAdress.as_view()),
    url(r'^modifyPhone/(?P<id>\d+)$', modifyPhone.as_view()),
    url(r'^modifyEmail/(?P<id>\d+)$', modifyEmail.as_view()),
    url(r'^show/(?P<id>\d+)$', PersonDetails.as_view()),
    url(r'^$', AllPerson.as_view()),
    url(r'^delete/(?P<id>\d+)$', PersonDelete.as_view()),
]
