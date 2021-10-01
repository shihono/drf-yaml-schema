# drf-yaml-schema

Custom AutoSchema for [django-rest-framework](https://www.django-rest-framework.org/)

Documenting your API with yaml format written in docstring.

Only support for [OpenAPI](https://github.com/OAI/OpenAPI-Specification) schema

## Usage

- Set `AutoYamlSchema` to View class's schema
- Write Operation Object (e.g. parameters, responses) to docstring in yaml format
   - Three or more horizontal bar (like `---`) mark the starting position of yaml

```
from rest_framework import views
from drf_yaml_schema import AutoYamlSchema

class YamlSchemaAPIView(views.APIView):
    schema = AutoYamlSchema()

    def get(self):
        """some comments
        ---
        parameters:
        - name: param
          in: query
          description: 
          ...
        """
```

- for more information, see [sample/](./sample/) project
