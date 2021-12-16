from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User



# Create your models here.

class Topic(models.Model):
   name = models.CharField(max_length=200)

   def __str__(self):
       return self.name


class Room (models.Model):
    name = models.CharField(max_length=200)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    update = models.TimeField(auto_now = True)
    create = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    update = models.TimeField(auto_now = True)
    create = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]