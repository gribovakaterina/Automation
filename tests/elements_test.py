import time
import allure

from selenium.webdriver.chrome.webdriver import WebDriver
from pages.elements_page import TextBoxPage

class TestElements:
    class TestTextBox:


        @allure.title('Заполнение полей "Elements"')
        @allure.tag('medium')
        def test_text_box(self, driver: WebDriver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            with allure.step('Проверка, что поле заполняется текстом с именем'):   
                assert full_name == output_name
            with allure.step('Проверка, что поле заполняется текстом с электронной почтой'):
                assert email == output_email
            with allure.step('Проверка, что поле заполняется текстом с адресом'):
                assert current_address == output_cur_addr
            assert permanent_address == output_per_addr