import random

import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

from diplom_users_tests.utils import attach


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def browser_setting():
    browser.config.base_url = "http://users.bugred.ru"
    browser.config.window_height = 1800
    browser.config.window_width = 1200

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        #"browserVersion": "",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f'https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub',
        options=options)

    browser.config.driver = driver

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture(scope="session")
def generated_user_data():
    name = "Даша"
    random_number = random.randint(1, 1000)
    random_name = f"{name}{random_number}"

    email = "test"
    random_email = f"{email}{random_number}@test.com"

    random_password = f"password{random_number}"

    user_data = {
        "name": random_name,
        "email": random_email,
        "password": random_password
    }

    return user_data
