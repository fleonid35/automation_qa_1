import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

#######################
# To check chromeDriverPath
# path = ChromeDriverManager().install()
# print(path)

# To upgrade DriverManager
# pip install - -upgrade webdriver - manager

# To use downloaded
#     # wd = webdriver.Chrome()
#     # return wd
