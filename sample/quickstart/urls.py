from django.urls import path

from rest_framework import routers
from rest_framework.schemas.views import SchemaView


router = routers.DefaultRouter(trailing_slash=False)


urlpatterns = [
    path("schema/", SchemaView.as_view())
]