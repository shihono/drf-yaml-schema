from re import I

from django.urls import path
from django.views.generic import TemplateView
from rest_framework import renderers, routers
from rest_framework.schemas.openapi import SchemaGenerator
from rest_framework.schemas.views import SchemaView

from .views import AutoSchemaAPIView, YamlSchemaAPIView

router = routers.DefaultRouter(trailing_slash=False)


urlpatterns = [
    path(
        "schema/",
        SchemaView.as_view(
            renderer_classes=[renderers.OpenAPIRenderer],
            schema_generator=SchemaGenerator(),
        ),
        name="schema",
    ),
    path(
        "swagger/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "schema"},
        ),
    ),
    path("auto-schema-api/", AutoSchemaAPIView.as_view()),
    path("yaml-schema-api/", YamlSchemaAPIView.as_view()),
]
