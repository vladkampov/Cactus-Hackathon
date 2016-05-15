from django.conf.urls import url
from stream.views import stream, stream_out, index, validate_photo

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^stream-out/$', stream_out, name='stream_out'),
    url(r'^stream/$', stream, name='stream'),
    url(r'^validate/photo/$', validate_photo, name='validate_photo'),
]
