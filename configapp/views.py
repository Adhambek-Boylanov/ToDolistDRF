from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count
from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from .make_token import get_tokens_for_user
from rest_framework.permissions import IsAuthenticated
class LoginUser(APIView):
    @swagger_auto_schema(request_body=LoginSerializers)
    def post(self,request):
        serializer = LoginSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(User,username = serializer.validated_data.get('username'))
        token = get_tokens_for_user(user)
        return Response(data=token)
class ToDoListApi(APIView):
    @swagger_auto_schema(request_body=UserSerializers)
    def post(self,request):
        serializer = UserSerializers(data=request.data)