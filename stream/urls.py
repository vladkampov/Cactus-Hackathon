from django.conf.urls import url
from stream.views import stream, stream_out, index, validate_photo, validate_captcha

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^stream-out/$', stream_out, name='stream_out'),
    url(r'^stream/(?P<pk>[0-9]+)$', stream, name='stream'),
    url(r'^validate/photo/$', validate_photo, name='validate_photo'),
    url(r'^validate/captcha/$', validate_captcha, name='validate_captcha'),
]
