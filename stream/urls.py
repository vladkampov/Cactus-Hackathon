from django.conf.urls import url
from stream.views import stream, stream_out, index, stream_final,\
	validate_photo, validate_captcha

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^stream-out/$', stream_out, name='stream_out'),
    url(r'^stream/(?P<pk>[0-9]+)$', stream, name='stream'),
    url(r'^stream_final/(?P<pk>[0-9]+)$', stream_final, name='stream_final_'),
    url(r'^validate/photo/$', validate_photo, name='validate_photo'),
    url(r'^validate/captcha/$', validate_captcha, name='validate_captcha'),
]
