from django.urls import path
from .views import catalogue, phone_detail
urlpatterns = [path("catalogue/", catalogue, name = "catalogue"),
               path("phone_detail/<slug:slug>/", phone_detail, name="phone_detail")]