from django.test import TestCase
from django.http import HttpRequest  
from block.views import home_page
from django.urls import resolve 
from block.models import Article
from datetime import datetime


class HomePageTests(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = home_page(request)  
        html = response.content.decode("utf8")  
        self.assertIn("<title>Стоматологічна клініка</title>", html)  
        self.assertIn("<h1>Studio Vita</h1>", html)
        self.assertTrue(html.startswith("<html>"))  
        self.assertTrue(html.endswith("</html>"))

    def test_home_page_displays_articles(self):
        Article.objects.create(
            title = 'title 1',
            summary = 'summary 1',
            full_text = 'full_text 1',
            pubdate = datetime.now(),
        )
        Article.objects.create(
            title = 'title 2',
            summary = 'summary 2',
            full_text = 'full_text 2',
            pubdate = datetime.now(),
        )

        request = HttpRequest()  
        response = home_page(request)
        html = response.content.decode("utf8")

        self.assertIn("title 1", html) 
        self.assertIn("summary 1", html)
        self.assertNotIn("text_full 1", html)  
        
        self.assertIn("title 2", html)  
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
            pubdate = datetime.now(),
        )
        article1.save()
        
        #створи статтю2
        #збережи статтю2
        article2 = Article(
            title = 'article 2',
            full_text = 'full_text 2',
            summary = 'summary 2',
            category = 'category 2',
            pubdate = datetime.now(),
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
        #перевірь: друга завантаження з бази стаття = стаття 2
        self.assertEqual(
            all_articles[1].title,
            article2.title
        )