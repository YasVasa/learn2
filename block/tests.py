from django.test import TestCase
from django.http import HttpRequest  
from block.views import home_page
from django.urls import resolve
from block.views import article_page
from block.models import Article
from datetime import datetime
from django.urls import reverse
import pytz

class ArticlePageTest(TestCase):

    def test_article_page_displays_correct_article(self):
        Article.objects.create(
            title = 'title 1',
            summary = 'summary 1',
            full_text = 'full_text 1',
            pubdate = datetime.utcnow().replace(tzinfo=pytz.utc),
            slug = 'slyg'
        )
      
        request = HttpRequest()  
        response =  article_page(request, 'slyg')
        html = response.content.decode("utf8")

        self.assertIn("title 1", html)
        self.assertIn("full_text 1", html)  
        self.assertNotIn("summary 1", html)

class HomePageTests(TestCase):

    def test_home_page_returns_correct_html(self):
        url = reverse('home_page')
        response = self.client.get(url)  
        self.assertTemplateUsed(response, 'home_page.html')

    def test_home_page_displays_articles(self):
        Article.objects.create(
            title = 'title 1',
            summary = 'summary 1',
            full_text = 'full_text 1',
            pubdate = datetime.utcnow().replace(tzinfo=pytz.utc),
            slug = 'slug-1'
        )
        Article.objects.create(
            title = 'title 2',
            summary = 'summary 2',
            full_text = 'full_text 2',
            pubdate = datetime.utcnow().replace(tzinfo=pytz.utc),
            slug = 'slug-2'
        )

        request = HttpRequest()  
        response = home_page(request)
        html = response.content.decode("utf8")

        self.assertIn("title 1", html)
        self.assertIn('/block/slug-1', html) 
        self.assertIn("summary 1", html)
        self.assertNotIn("text_full 1", html)  
        
        self.assertIn("title 2", html)  
        self.assertIn('/block/slug-2', html)
        self.assertIn("summary 2", html)
        self.assertNotIn("text_full 2", html)

class ArticleModelTest(TestCase):
    
    def test_article_model_save_and_retrieve(self):
        #створи статтю1
        #збережи статтю1
        article1 = Article(
            title = 'article 1',
            full_text = 'full_text 1',
            summary = 'summary 1',
            category = 'category 1',
            pubdate = datetime.utcnow().replace(tzinfo=pytz.utc),
            slug = 'slug-1'
        )
        article1.save()
        
        #створи статтю2
        #збережи статтю2
        article2 = Article(
            title = 'article 2',
            full_text = 'full_text 2',
            summary = 'summary 2',
            category = 'category 2',
            pubdate = datetime.utcnow().replace(tzinfo=pytz.utc),
            slug = 'slug-2'
        )
        article2.save()

        #завантаж з бази всі статті
        all_articles = Article.objects.all()

        #перевірь: їх повинно бути дві
        self.assertEqual(len(all_articles), 2)
        #перевірь: перша завантаження з бази стаття = стаття 1
        self.assertEqual(
            all_articles[0].title,
            article1.title
        )
        self.assertEqual(
            all_articles[0].slug,
            article1.slug
        )
        #перевірь: друга завантаження з бази стаття = стаття 2
        self.assertEqual(
            all_articles[1].title,
            article2.title
        )
        self.assertEqual(
            all_articles[1].slug,
            article2.slug
        )
