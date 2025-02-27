from django.urls import path
from .views import apod, mars_photos

urlpatterns = [
    path("apod/", apod, name="apod"),
    path("mars-photos/", mars_photos, name="mars_photos"),
]
