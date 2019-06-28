from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import User

from django.conf import settings

class Category(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return "%s %s" % (self.name)
class Post(models.Model):
    user_id = models.IntegerField()
    # category_id = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, default='')
    file = models.TextField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('created',)
