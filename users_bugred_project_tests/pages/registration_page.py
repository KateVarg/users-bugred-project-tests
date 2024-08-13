from selene import browser, be, have
import allure
from users_bugred_project_tests.data.users_login import UserForRegistration


class UserRegistration:

    @allure.step('Открытие сайта')
    def open(self):
        browser.open('/user/login/index.html')
        return self

    @allure.step('Ввод имени')
    def fill_name(self, name):
        browser.element('[name="name"]').type(name)
        return self

    @allure.step('Ввод email')
    def fill_email(self, email):
        browser.element('[name="email"]').type(email)
        return self

    @allure.step('Ввод пароля')
    def fill_password(self, password):
        browser.element('[action*="register"] [name="password"]').type(password)
        return self

    @allure.step('Нажатие на кнопку Зарегистрироваться')
    def click_registration_button(self):
        browser.element('[action*="register"] [name="act_register_now"]').click()
        return self

    @allure.step('Проверка успешной регистрации')
    def check_success_registration(self):
        browser.element('.navbar-nav').should(be.visible)
        return self

    @allure.step('Проверка ошибки при незаполнении обязательного поля Имя')
    def check_required_name(self):
        browser.element('[name="name"]').should(have.attribute('validationMessage').value('Please fill out this field.'))
        return self

    @allure.step('Проверка ошибки при незаполнении обязательного поля Email')
    def check_required_email(self):
        browser.element('[name="email"]').should(have.attribute('validationMessage').value('Please fill out this field.'))
        return self

    @allure.step('Проверка ошибки при незаполнении обязательного поля Пароль')
    def check_required_password(self):
        browser.element('[action*="register"] [name="password"]').should(have.attribute('validationMessage').value('Please fill out this field.'))
        return self

    @allure.step('Заполнение полей в форме')
    def fill_registration_form(self, user: UserForRegistration):
        self.fill_name(user.name).fill_email(user.email).fill_password(user.password).click_registration_button()


user_registration = UserRegistration()
