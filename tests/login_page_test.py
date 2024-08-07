import pytest
import allure
from diplom_users_tests.data.users_login import UserForLogin, UserForRegistration
from diplom_users_tests.pages.login_page import user_login, user_registration


@allure.feature("Авторизация")
@allure.story("Успешная авторизация")
@allure.title("Успешная авторизация пользователя")
@pytest.mark.order(2)
def test_success_login(generated_user_data):
    user = UserForLogin(
        generated_user_data['email'],
        generated_user_data['password']
    )
    user_login.open().success_login(user)


@allure.feature("Авторизация")
@allure.story("Неуспешная авторизация")
@allure.title("Неуспешная авторизация пользователя")
@pytest.mark.order(2)
@pytest.mark.xfail
def test_login_fail():
    user = UserForLogin(
        'test@test.com',
        '123456789'
    )
    user_login.open().login_fail(user)


@allure.feature("Регистрация")
@allure.story("Успешная регистрация")
@allure.title("Регистрация нового пользователя")
@pytest.mark.order(1)
def test_success_user_registration(generated_user_data):
    user = UserForRegistration(
        generated_user_data['name'],
        generated_user_data['email'],
        generated_user_data['password']
    )

    user_registration.open().fill_registration_form(user)
    user_registration.check_success_registration()


@allure.feature("Регистрация")
@allure.story("Проверка обязательных полей")
@allure.title("Проверка обязательности поля name")
@pytest.mark.order(1)
def test_required_input_name():
    user = UserForRegistration(
        '',
        'test@test.com',
        'password123'
    )
    user_registration.open().fill_registration_form(user)
    user_registration.check_required_name()


@allure.feature("Регистрация")
@allure.story("Проверка обязательных полей")
@allure.title("Проверка обязательности поля email")
@pytest.mark.order(1)
def test_required_input_email():
    user = UserForRegistration(
        'Роман',
        '',
        'password123'
    )
    user_registration.open().fill_registration_form(user)
    user_registration.check_required_email()


@allure.feature("Регистрация")
@allure.story("Проверка обязательных полей")
@allure.title("Проверка обязательности поля password")
@pytest.mark.order(1)
def test_required_input_password():
    user = UserForRegistration(
        'Роман',
        'test@test.com',
        ''
    )
    user_registration.open().fill_registration_form(user)
    user_registration.check_required_password()
