from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib.auth import get_user_model


class Courses(models.Model):
    cid=models.PositiveIntegerField(primary_key=True)
    title=models.TextField()
    description=models.TextField()
    slug=models.SlugField()
    videourl=models.TextField()
    thumb=models.FileField(upload_to="thumb/%y",blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    CommentPost = models.ForeignKey(Courses , on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE , related_name='replies')

    class Meta:
        ordering=['-date_posted']

    def __str__(self):
        return str(self.author) + ' comment ' + str(self.content)

    @property
    def children(self):
        return Comment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False 

class JoinedCourses(models.Model):
    courseName=models.TextField()
    profileid=models.PositiveIntegerField()
    courseid=models.PositiveIntegerField()
    
    def __str__(self):
        return self.courseName