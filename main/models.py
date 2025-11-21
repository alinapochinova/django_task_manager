from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
    null=True, blank=True)
    executor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
    blank=True)
    def __str__(self):
        return self.title
# Create your models here.
