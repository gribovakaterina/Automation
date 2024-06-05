import time
import allure

from selenium.webdriver.chrome.webdriver import WebDriver
from pages.elements_page import CheckBoxPage, TextBoxPage

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
            with allure.step('Проверка, что поле заполняется текстом с текущим адресом'):
                assert current_address == output_cur_addr
            with allure.step('Проверка, что поле заполняется текстом с постоянным адресом'):
                assert permanent_address == output_per_addr

    class TestCheckBox:
        @allure.title('Заполнение чек-боксов')
        @allure.tag('hard')
        def test_check_box(self, driver: WebDriver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_cheked_checkboxes()
            output_result = check_box_page.get_output_result()

            with allure.step('Проверка одинаковых значений'):
                assert input_checkbox == output_result, 'chekboxes have not been selected'