from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=30)
    full_text = models.TextField()
    summary = models.CharField(max_length=225)
    category = models.CharField(max_length=30)
    pubdate = models.DateTimeField()
    slug = models.CharField(max_length=225, unique=True)
    #is_published = models.BooleanField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_page', kwargs={'slug': self.slug})
    
#class About(models.Model):



    #Написати функцію пошуку
    #Контакти
    #Сторінку колективу(або Про нас)
    #Розділи
    