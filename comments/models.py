from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from posts.models import Post

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True,editable=False,default=uuid4)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
        
        
class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comment')
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()

  def __str__(self):
    return f"Comment on '{self.post.title}' by {self.author.username}" 

  
  class Meta:
      db_table = "comments"