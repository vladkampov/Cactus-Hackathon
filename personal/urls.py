from django.conf.urls import url
from personal.views import registration

urlpatterns = [
    url(r'^login/', registration, name='login'),
]
