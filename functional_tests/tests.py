import unittest
from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from datetime import datetime
import pytz
from block.models import Article


class BasicInstallTest(LiveServerTestCase):  

    # Ввівши в Гуглі запит стоматологічна клініка Італія (in Italy)
    # Користувач переходить по ссиліці і перейшов на сайт 'Vita Studio'
    def setUp(self): 
        self.driver = webdriver.Chrome()
        Article.objects.create(
            title = 'title 1',
            summary = 'summary 1',
            full_text = 'full_text 1',
            pubdate = datetime.utcnow().replace(tzinfo=pytz.utc),
            slug = 'slyg'
        )

    def tearDown(self):
        self.driver.quit()

    def test_home_page_title(self):
        # Перейшовши за адрессою "self.life_server_url" користувач бачить загаловок сайту 'Стоматологічна клініка'
        self.driver.get(self.live_server_url) 
        self.assertIn("Стоматологічна клініка", self.driver.title)  
        # self.fail("Finish the test!") 

    def test_home_page_header(self): 
        # Прочитавшо заголовок користувач бачить назву клініки 'Vita Studio'
        self.driver.get(self.live_server_url)
        header = self.driver.find_element(By.TAG_NAME, 'h1')
        self.assertIn("Studio Vita", header.text)  
        #self.fail("Finish the test!")  

    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        header = self.driver.find_element(By.TAG_NAME, 'h1')

        self.assertTrue(header.location["x"]> 10)

    def test_home_page_blog(self):
        # Під шопкою сайту знаходиться блок з статтями
        self.driver.get(self.live_server_url)
        article_list = self.driver.find_element(By.CLASS_NAME, 'article-list')
        self.assertTrue(article_list)

    def test_home_page_articles_look_correct(self):
 
        # В кожної статті є заголовок і один абзац з текстом
        self.driver.get(self.live_server_url)
        article_title = self.driver.find_element(By.CLASS_NAME, 'article-title')
        article_summary = self.driver.find_element(By.CLASS_NAME, 'article-summary')
        self.assertTrue(article_title) 
        self.assertTrue(article_summary)   

    def test_home_page_article_title_link_leads_to_article_page(self):
        # Після кліку по заголовку відкривається сторінка з повним текстом
        # Відкриваємо головну сторінку
        self.driver.get(self.live_server_url)
        # Знаходимо статтю 
        # Знаходимо заголовок статті                                            
        article_title = self.driver.find_element(By.CLASS_NAME, 'article-title')
        article_title_text = article_title.text
        # Знаходимо ссилку в заголовці
        article_link = article_title.find_element(By.TAG_NAME, 'a')
        # переходимо по ссилці
        self.driver.get(article_link.get_attribute('href'))
        # Бачимо повну статтю
        article_page_title = self.driver.find_element(By.CLASS_NAME, 'article-title')

        self.assertEqual(article_title_text, article_page_title.text)

  
