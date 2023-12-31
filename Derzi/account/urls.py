from django.urls import path
from account import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name = "signup"),
    path('login/', views.LoginUserViews.as_view(), name = "login"),
    path('logout/', views.LogoutViews.as_view(), name = "logout")
]