from django.urls import path,include
from .views import PostView,PostList,UpdatePost,DeletePost

urlpatterns = [
    
    path('create/',PostView.as_view()),
    path('list/',PostList.as_view()),
    path('edit/',UpdatePost.as_view()),
    path('delete/',DeletePost.as_view()),
]