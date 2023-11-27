import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from register_new_user import register_new_user_return_login_pass_and_response
from data import Urls, Endpoints


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    data = register_new_user_return_login_pass_and_response()
    yield data[0]
    access_token = data[1].json()["accessToken"]
    requests.delete(f'{Urls.URL_SB}{Endpoints.DELETE_USER}', headers={'Authorization': f'{access_token}'})
