from selenium import webdriver
from django.test import TestCase
import unittest


# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')
#
# assert 'Todo' in browser.title

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_getaccess_and_retrieve(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('to', self.browser.title)
        # self.fail('try again')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
