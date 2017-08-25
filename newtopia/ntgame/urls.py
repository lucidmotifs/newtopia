from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^throne/', views.throne, name='throne'),
    url(r'^build/', views.build, name='build')
]
