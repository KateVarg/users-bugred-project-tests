import pytest
import allure
from users_bugred_project_tests.data.users_login import UserForLogin
from users_bugred_project_tests.pages.login_page import user_login


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
    user_login.open().fail_login(user)
