from django.contrib.auth.models import User # User 모델
from django.contrib.auth.password_validation import validate_password
from .models import location, SubCategory, foodends, koreafoods
# Django의 기본 패스워드 검증 도구

from rest_framework import serializers
from rest_framework.authtoken.models import Token # Token 모델
# from rest_framework.validators import UniqueValidator # 이메일 중복 방지를 위한 검증 도구
from django.contrib.auth import authenticate
from .models import Page

class RegisterSerializer(serializers.ModelSerializer): # 회원가입 시리얼라이저
    # email = serializers.EmailField(
    #     required=True,
        # validators=[UniqueValidator(queryset=User.objects.all())], # 이메일에 대한 중복 검증
    # )
    password = serializers.CharField(
        write_only = True,
        required=True,
        validators=[validate_password], # 비밀번호 확인을 위한 필드
    )
    password2 = serializers.CharField(write_only = True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'last_name')

    def validate(self, data): # 추가적으로 비밀번호 일치 여부를 확인
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return data

    def create(self, validated_data): # CREATE 요청에 대해 create 메소드를 오버라이딩, 유저를 생성하고 토큰을 생성하게 함.
        user = User.objects.create_user(
            username=validated_data['username'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer): # 로그인
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user: # 유저 찾기
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError(
            {"error": "Unable to log in with provided credentials."})

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ("like1", "like2", "like3")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'last_name')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = location
        fields = ('name','location','score')

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class KoreaFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = koreafoods
        fields = '__all__'


class FoodEndSerializer(serializers.ModelSerializer):
    class Meta:
        model = foodends
        fields = '__all__'
