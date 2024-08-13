from users_bugred_project_tests.data.data_search import SearchUser
from users_bugred_project_tests.pages.users_page import user_search
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
