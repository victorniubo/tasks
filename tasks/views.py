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


@api_view(["GET"])
def taskGet(request):
    data = TaskSerializer(Task.objects.all(), many=True)
    return JsonResponse(data.data, safe=False)


@api_view(["POST"])
def taskPost(request):
    data = JSONParser().parse(request)
    serializer = TaskSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors, status=400)


@api_view(["DELETE"])
def taskDelete(request):
    Task.objects.all().delete()
    return HttpResponse("Tasks deletadas")