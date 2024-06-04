import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chromeService

@pytest.fixture(scope = 'function')
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("-headless")
    driver_service = chromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()