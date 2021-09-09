from inspect import cleandoc

from rest_framework.schemas.openapi import AutoSchema
from rest_framework.utils import formatting

import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


class AutoYamlSchema(AutoSchema):
    def __init__(self, tags=None, operation_id_base=None, component_name=None):
        super().__init__(tags, operation_id_base, component_name)

        self.yaml_schemas = {}
        for method in self.view.http_method_names:
            self.yaml_schemas[method] = self.get_yaml_from_docstring(method)


    def get_yaml_from_docstring(self, method):
        """get operation object yaml data from docstring
        `---` を起点として読み込む
        """
        view = self.view
        method_name = str(method).lower()
        if not hasattr(view, method_name):
            return None

        docstring = getattr(view, method_name).__doc__
        split_lines = cleandoc(docstring).split("\n")
        # Cut YAML from rest of docstring
        for index, line in enumerate(split_lines):
            line = line.strip()
            if line.startswith("---"):
                cut_from = index
                break
        else:
            return None
        yaml_string = "\n".join(split_lines[cut_from:])
        yaml_string = formatting.dedent(yaml_string)
        try:
            return yaml.load(yaml_string, Loader=Loader)
        except yaml.YAMLError:
            return None

    def get_operation(self, method):
        # todo SchemaGenerator が呼び出す関数
        if self.yaml_schemas:
            return self.yaml_schemas[method]
        else:
            return super().get_operation(method)


    def get_components(self, path, method):
        # todo SchemaGenerator が呼び出す関数
        if self.yaml_schemas:
            return {}
        return super().get_components(path, method)
