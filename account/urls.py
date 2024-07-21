from django.urls import path,include
from .views import RegisterUserView,Login

urlpatterns = [
    
    path('register/',RegisterUserView.as_view()),
    path('login/',Login.as_view()),
]