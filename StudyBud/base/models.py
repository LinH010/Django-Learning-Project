from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name =models.CharField(max_length=200,null=True)
    email =models.EmailField(unique=True,null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(default="avatar.svg")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

# Create your database models here.
# example:
# class Project(models.Model):         like: attribute = models.type()
# title = models.CharField)
# description = models.TextField()
# id = models.UUIDField()

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # SET_NULL: when the parent table item is deleted, message item that connecting it become null
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    # null = true: databases description can be blank. blank = True: forms description can be blank
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User,related_name='participants',blank=True)
    updated = models.DateTimeField(auto_now=True)  # when every time save,update this
    created = models.DateTimeField(auto_now_add=True)  # when first time save,update this

    class Meta:
        # parameter 1,2 ascending: higher level  p1 > p2
        ordering = ['-updated','-created']
    def __str__(self):
        return self.name


class Message(models.Model):
    # ForeignKey(parentTable,options)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # models.CASCADE:when the parent table item is deleted, message item that connecting it gets deleted
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)  # when every time save,update this
    created = models.DateTimeField(auto_now_add=True)  # when first time save,update this
    class Meta:
        # parameter 1,2 ascending: higher level  p1 > p2
        ordering = ['-updated','-created']
    def __str__(self):
        return self.body[0:50]
