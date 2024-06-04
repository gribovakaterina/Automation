import time
from pages.base_page import BasePage

def test(driver):
    page = BasePage(driver, 'https://www.google.com/')
    page.open()
    time.sleep(3)

def test_yandex(driver):
    page = BasePage(driver, 'https://ya.ru/')
    page.open()
    time.sleep(3)    