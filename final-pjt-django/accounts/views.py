from django.shortcuts import render
from .models import User
from .serializers import ProfileSerializer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404

@api_view(['GET'])
def myprofile(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'GET':
        serializer = ProfileSerializer(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ProfileSerializer(user,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)