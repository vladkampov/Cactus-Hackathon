from django.conf.urls import url
from personal.views import registration

urlpatterns = [
    url(r'^registration/(?P<type>\w+)', registration, name='registration'),
]
