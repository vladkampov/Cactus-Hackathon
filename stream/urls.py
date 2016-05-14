from django.conf.urls import url
from stream.views import index, stream

urlpatterns = [
    url(r'^$', stream, name='stream'),
]
