from django.test import TestCase
from django.http import HttpRequest  
from block.views import home_page
from django.urls import resolve 


class HomePageTests(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = home_page(request)  
        html = response.content.decode("utf8")  
        self.assertIn("<title>Стоматологічна клініка</title>", html)  
        self.assertIn("<h1>Studio Vita/h1>", html)
        self.assertTrue(html.startswith("<html>"))  
        self.assertTrue(html.endswith("</html>"))  