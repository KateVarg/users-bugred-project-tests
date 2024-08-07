import requests
from selene import browser, be, query, have
import allure
from diplom_users_tests.data.users_login import UserForLogin, UserForRegistration


class UserLogin:

    @allure.step('Открытие сайта')
    def open(self):
        browser.open('/user/login/index.html')
        return self

    @allure.step('Ввод email')
    def fill_email(self, email):
        browser.element('input[name="login"]').type(email)
        return self

    @allure.step('Ввод пароля')
    def fill_password(self, password):
        browser.element('input[name="password"]').type(password)
        return self

    @allure.step('Нажатие на кнопку Авторизоваться')
    def click_login_button(self):
        browser.element('input[value="Авторизоваться"]').click()
        return self

    @allure.step('Проверка успешной авторизации')
    def check_success_login(self):
        browser.element('.navbar-nav').should(be.visible)
        return self

    @allure.step('Проверка неуспешной авторизации')
    def check_fail_login(self):
        browser.element('.row').should(have.text('Невереный логин или пароль'))
        return self

    @allure.step('Успешная авторизация')
    def success_login(self, user: UserForLogin):
        self.fill_email(user.email).fill_password(user.password).click_login_button().check_success_login()

    @allure.step('Неуспешная авторизация')
    def fail_login(self, user: UserForLogin):
        self.fill_email(user.email).fill_password(user.password).click_login_button().check_fail_login()


user_login = UserLogin()


class UserRegistration:

    @allure.step('Открытие сайта')
    def open(self):
        browser.open('/user/login/index.html')
        return self

    @allure.step('Ввод имени')
    def fill_name(self, name):
        browser.element('input[name="name"]').type(name)
        return self

    @allure.step('Ввод email')
    def fill_email(self, email):
        browser.element('input[name="email"]').type(email)
        return self

    @allure.step('Ввод пароля')
    def fill_password(self, password):
        browser.element('form[action="/user/register/index.html"] input[name="password"]').type(password)
        return self

    @allure.step('Нажатие на кнопку Зарегистрироваться')
    def click_registration_button(self):
        browser.element('form[action="/user/register/index.html"] input[name="act_register_now"]').click()
        return self

    @allure.step('Проверка успешной регистрации')
    def check_success_registration(self):
        browser.element('.navbar-nav').should(be.visible)
        return self

    @allure.step('Проверка ошибки при незаполнении обязательного поля Имя')
    def check_required_name(self):
        browser.element('input[name="name"]').should(have.attribute('validationMessage', 'Please fill out this field.'))
        return self

    @allure.step('Проверка ошибки при незаполнении обязательного поля Email')
    def check_required_email(self):
        browser.element('input[name="email"]').should(have.attribute('validationMessage', 'Please fill out this field.'))
        return self

    @allure.step('Проверка ошибки при незаполнении обязательного поля Пароль')
    def check_required_password(self):
        browser.element('form[action="/user/register/index.html"] input[name="password"]').should(have.attribute('validationMessage', 'Please fill out this field.'))
        return self

    @allure.step('Заполнение полей в форме')
    def fill_registration_form(self, user: UserForRegistration):
        self.fill_name(user.name).fill_email(user.email).fill_password(user.password).click_registration_button()


user_registration = UserRegistration()


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
        print(self.response.status_code)
        assert self.response.status_code == 302
        return self

    @allure.step('Получение cookie')
    def get_cookie(self):
        print(self.response.cookies)
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
