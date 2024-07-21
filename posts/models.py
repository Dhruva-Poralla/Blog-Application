from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True,editable=False,default=uuid4)
    published_date = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
        
        

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="post")
    title = models.CharField(max_length=500)
    content = models.TextField()
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table  = "posts"
    
    
    