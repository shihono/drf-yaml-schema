from rest_framework import views
from rest_framework.schemas.openapi import AutoSchema

from drf_yaml_schema.schema import AutoYamlSchema


class AutoSchemaAPIView(views.APIView):
    http_method_names = ["get"]
    schema = AutoSchema()

    def get(self):
        pass


class YamlSchemaAPIView(views.APIView):
    http_method_names = ["get"]
    schema = AutoYamlSchema()

    def get(self):
        """
        ---
        parameters:
        - name: limit
          in: query
          description: How many items to return at one time (max 100)
          required: false
          schema:
            type: integer
        responses:
        '200':
          description: A paged array of pets
          headers:
            x-next:
              description: A link to the next page of responses
              schema:
                type: string
          content:
            application/json:
              schema:
                type: integer
        """
        pass
