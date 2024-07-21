from django.urls import path,include
from .views import CommentView,CommentListView

urlpatterns = [
    
    path('create/',CommentView.as_view()),
    path('list/',CommentListView.as_view()),
]