from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^getCourse', views.getCourse),
    url(r'^courses/destroy/(?P<id>\d+)', views.destroy),
    url(r'^delete', views.delete)
]