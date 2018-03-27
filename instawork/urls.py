from django.conf.urls import *
from instaworkapi.views import listings


urlpatterns = [
 url(r'^$', listings.as_view(), name='my_rest_view'),
]
