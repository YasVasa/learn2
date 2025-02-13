import unittest
from selenium import webdriver


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
        self.assertIn("Стоматологічна клініка ", self.browser.title)  
        #self.fail("Finish the test!") 

    def test_home_page_header(self):  
        # прочитавшо заголовок користувач бачить назву клініки 'Vita Studio'
        browser = self.browser.get("http://127.0.0.1:8000")
        header = browser.find_elements_by_tag_name('h1')[0]  
        self.assertIn("Vita Studio", header)  
        #self.fail("Finish the test!")  

if __name__ == "__main__":  
    unittest.main()  