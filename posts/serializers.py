from rest_framework import serializers
from .models import Post
from comments.models import Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "author",
            "content"
        ]