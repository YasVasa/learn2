from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=30)
    full_text = models.TextField()
    summary = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    pubdate = models.DateTimeField()
    #is_published = models.BooleanField()