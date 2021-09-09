from django.shortcuts import render
from rest_framework import views


class ConvertView(views.APIView):
    http_method_names = ["get"]
    def get(self):
        pass