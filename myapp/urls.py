from django.urls import path
from .models import Person

from . import views

urlpatterns = [
    path("", views.index),
    path("create/", views.create, name="create"),
]