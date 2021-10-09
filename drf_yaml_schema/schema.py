from inspect import cleandoc

import yaml
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.utils import formatting

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


class AutoYamlSchema(AutoSchema):
    def __init__(self, tags=None, operation_id_base=None, component_name=None):
        super().__init__(tags, operation_id_base, component_name)
        self.yaml_schemas = {}

    def load_yaml_from_docstring(self, method):
        """load operation object yaml data from docstring
        `---` is starting point to load yaml
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

    def get_yaml_from_docstring(self, method):
        if self.yaml_schemas.get(method):
            return self.yaml_schemas[method]
        self.yaml_schemas[method] = self.load_yaml_from_docstring(method)
        return self.yaml_schemas[method]

    def get_operation(self, path, method):
        """get Operation Object on a path from method's docstring"""
        if self.get_yaml_from_docstring(method):
            return self.yaml_schemas[method]
        else:
            return super().get_operation(path, method)

    def get_components(self, path, method):
        """get Components Object
        if get operation object from docstring, return None
        """
        if self.get_yaml_from_docstring(method):
            return {}
        return super().get_components(path, method)
