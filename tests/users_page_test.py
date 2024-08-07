from diplom_users_tests.data.data_search import SearchUser
from diplom_users_tests.pages.users_page import user_search, open_profile_page
import allure


@allure.feature("Список пользователей")
@allure.story("Поиск пользователя")
@allure.title("Поиск существующего пользователя")
def test_search_user():
    user = SearchUser(
        '2018',
        '08',
        '14',
        '2019',
        '08',
        '19',
        'Красавчик'
    )
    user_search.open().register(user).check_search_result(user)


@allure.feature("Список пользователей")
@allure.story("Профиль пользователя")
@allure.title("Переход на страницу с профилем пользователя")
def test_open_profile_page():
    open_profile_page.open().click_show_button().check_profile()


