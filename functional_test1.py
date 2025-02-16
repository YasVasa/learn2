import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class BasicInstallTest(unittest.TestCase):  

# Ввівши в Гуглі запит стоматологічна клініка Італія (in Italy)
# Користувач переходить по ссиліці і перейшов на сайт 'Vita Studio'
    def setUp(self):  
        self.browser = webdriver.Chrome()  

    def tearDown(self):  
        self.browser.quit()

    def test_home_page_title(self):  
        # Перейшовши за адрессою "http://127.0.0.1:8000" користувач бачить загаловок сайту 'Стоматологічна клініка'
        self.browser.get("http://127.0.0.1:8000") 
        self.assertIn("Стоматологічна клініка", self.browser.title)  
        #self.fail("Finish the test!") 

    def test_home_page_header(self):  
        # прочитавшо заголовок користувач бачить назву клініки 'Vita Studio'
        self.browser.get("http://127.0.0.1:8000")
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn("Studio Vita", header.text)  
        #self.fail("Finish the test!")  

    def test_home_page_ponts(self):
        # під заголовкома є пункти переваг 
        self.browser.get("http://127.0.0.1:8000")
        points  = self.browser.find_element_by_class_name('points')
        self.assertTrue(points)

        
if __name__ == "__main__":  
    unittest.main()  