from django.urls import path
from .views import RegisterView, LoginView, PageView, DeleteAPIView, UserView
from .views import LocationList, MenuList, KoreaFood, FoodEnd
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('page/<int:pk>/', PageView.as_view()),
    path('delete/<int:pk>/', DeleteAPIView.as_view()),
    path('user/<int:pk>/', UserView.as_view()),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('location/', LocationList.as_view()),
    path('menu/', MenuList.as_view()),
    path('koreafoods/', KoreaFood.as_view()),
    path('foodends/', FoodEnd.as_view()),

]