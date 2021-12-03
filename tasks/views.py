from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from tasks.models import Task
from django.core import serializers
from django.forms.models import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from tasks.serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
# Create your views here.


@api_view(["GET"])
def getTasks(request):
    task = Task.objects.all()
    task_json = serializers.serialize("json", task)
    return HttpResponse(task_json, content_type="application/json")


@api_view(["POST"])
def createTask(request):
    print(request)
    infoJson = JSONParser().parse(request)
    print(infoJson)
    serializer_class = TaskSerializer(data=infoJson)
    if serializer_class.is_valid():
        serializer_class.save()
        return JsonResponse(serializer_class.data, status=201)
    return JsonResponse(serializer_class.errors, status=400)