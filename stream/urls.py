from django.conf.urls import url
from stream.views import stream, index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^stream/$', stream, name='stream'),
]
