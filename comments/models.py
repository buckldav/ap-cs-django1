from django.db import models

# Create your models here.
class Posts(models.Model):
  pass

class Comment(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  comment = models.TextField()
  name = models.CharField(max_length=100)

  _post = models.ForeignKey(to=Posts, on_delete=models.CASCADE)
  
  class Meta:
    ordering = ['created']