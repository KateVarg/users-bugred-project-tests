import requests
from selene import browser
import allure


class UserLoginAPI:

    @allure.step('Авторизация через api')
    def login_api(self, generated_user_data):
        url_login_api = 'http://users.bugred.ru/user/login/'
        email = generated_user_data['email']
        password = generated_user_data['password']
        self.response = requests.post(
            url=url_login_api,
            data={"login": email, "password": password},
            allow_redirects=False
        )
        return self

    @allure.step('Проверка кода')
    def check_code(self):
        assert self.response.status_code == 302
        return self

    @allure.step('Получение cookie')
    def get_cookie(self):
        self.cookie1 = self.response.cookies.get("misterti")
        self.cookie2 = self.response.cookies.get("PHPSESSID")
        return self

    @allure.step('Добавление cookie')
    def add_cookie(self):
        browser.open('/user/login/index.html')
        browser.driver.add_cookie({"name": "misterti", "value": self.cookie1})
        browser.driver.add_cookie({"name": "PHPSESSID", "value": self.cookie2})
        browser.open('/user/login/index.html')
        return self

    @allure.step('Перезагрузка браузера')
    def refresh_browser(self):
        browser.driver.refresh()
        return self


user_login_api = UserLoginAPI()
