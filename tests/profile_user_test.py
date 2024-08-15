from users_bugred_project_tests.pages.profile_user_page import profile_user_page
import allure


@allure.feature("Список пользователей")
@allure.story("Профиль пользователя")
@allure.title("Переход на страницу с профилем пользователя")
def test_open_profile_page():
    profile_user_page.open().click_show_button().check_profile()


