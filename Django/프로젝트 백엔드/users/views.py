from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer, PageSerializer, UserSerializer, LocationSerializer, FoodEndSerializer, KoreaFoodSerializer
from .models import Page , location, SubCategory,koreafoods,foodends
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from django.contrib.auth.decorators import login_required
from . import serializers
# Create your views here.


class RegisterView(generics.CreateAPIView): # CreateAPIView(generics) 사용 구현
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"token": token.key}, status=status.HTTP_200_OK)

# RetrieveUpdateAPIView 데이터 조회, 데이터 수정
class PageView(generics.RetrieveUpdateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class UserView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Delete View 탈퇴
# 삭제할 시, 형식을 지정할 필요가 없으므로, Serializer_class는 필요없음
class DeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()


class LocationList(APIView):
    def get(self, request, format=None):
        questions = location.objects.all()
        serializer = serializers.LocationSerializer(questions, many=True)
        return Response(serializer.data)

class MenuList(APIView):
    def get(self, request, format=None):
        questions = SubCategory.objects.all()
        serializer = serializers.MenuSerializer(questions, many=True)
        return Response(serializer.data)

class KoreaFood(APIView):
    def get(self, request, format=None):
        questions = koreafoods.objects.all()
        serializer = serializers.KoreaFoodSerializer(questions, many=True)
        return Response(serializer.data)

class FoodEnd(APIView):
    def get(self, request, format=None):
        questions = foodends.objects.all()
        serializer = serializers.FoodEndSerializer(questions, many=True)
        return Response(serializer.data)