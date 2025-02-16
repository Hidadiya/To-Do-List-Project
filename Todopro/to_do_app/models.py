from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50,null=True)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.name



