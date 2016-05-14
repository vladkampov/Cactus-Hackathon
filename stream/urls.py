from django.conf.urls import url
from stream.views import stream

urlpatterns = [
    url(r'^$', stream, name='stream'),
]
