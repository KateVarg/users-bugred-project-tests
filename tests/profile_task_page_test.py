from users_bugred_project_tests.data.profile_task import Task
from users_bugred_project_tests.pages.profile_tasks_page import add_task
from users_bugred_project_tests.pages.login_API_page import user_login_api
import allure


@allure.feature("Добавление новой задачи")
@allure.story("Переход на страницу добавления новой задачи")
@allure.title("Проверка перехода на страницу добавления новой задачи")
def test_open_page_add_task(generated_user_data):
    user_login_api.login_api(generated_user_data).check_code().get_cookie()
    user_login_api.add_cookie()
    add_task.open_list_tasks().click_button_add_task().check_open_page_add_task()


@allure.feature("Добавление новой задачи")
@allure.story("Добавление новой задачи")
@allure.title("Проверка добавления новой задачи")
def test_add_task(generated_user_data):
    user_login_api.login_api(generated_user_data).check_code().get_cookie()
    user_login_api.add_cookie()
    task = Task(
        'Test Task',
        'Test description'
    )
    add_task.open_add_task().add_task(task)
    add_task.check_add_task(task)
