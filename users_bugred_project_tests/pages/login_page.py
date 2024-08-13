import requests
from selene import browser, be, query, have
import allure
from users_bugred_project_tests.data.users_login import UserForLogin, UserForRegistration


class UserLogin:

    @allure.step('Открытие сайта')
    def open(self):
        browser.open('/user/login/index.html')
        return self

    @allure.step('Ввод email')
    def fill_email(self, email):
        browser.element('[name="login"]').type(email)
        return self

    @allure.step('Ввод пароля')
    def fill_password(self, password):
        browser.element('[name="password"]').type(password)
        return self

    @allure.step('Нажатие на кнопку Авторизоваться')
    def click_login_button(self):
        browser.element('.btn.btn-danger, [value="Авторизоваться]').click()
        return self

    @allure.step('Проверка успешной авторизации')
    def check_success_login(self):
        browser.element('.navbar-nav').should(be.visible)
        return self

    @allure.step('Проверка неуспешной авторизации')
    def check_fail_login(self):
        browser.element('.row').should(have.text('Неверный логин или пароль'))
        return self

    @allure.step('Успешная авторизация')
    def success_login(self, user: UserForLogin):
        self.fill_email(user.email).fill_password(user.password).click_login_button().check_success_login()

    @allure.step('Неуспешная авторизация')
    def fail_login(self, user: UserForLogin):
        self.fill_email(user.email).fill_password(user.password).click_login_button().check_fail_login()


user_login = UserLogin()
