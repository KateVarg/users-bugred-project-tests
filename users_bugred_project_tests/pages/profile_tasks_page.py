from selene import browser, query, have
import allure
from users_bugred_project_tests.data.profile_task import Task


class AddTask:

    @allure.step('Открытие страницы со списком задач пользователя')
    def open_list_tasks(self):
        browser.open('/tasks')
        return self

    @allure.step('Нажатие на кнопку Добавить задачу')
    def click_button_add_task(self):
        browser.element('a.btn.btn-warning').click()
        return self

    @allure.step('Проверка перехода на страницу добавления задачи')
    def check_open_page_add_task(self):
        browser.element('h2').should(have.text('Добавление задачи'))
        return self

    @allure.step('Открытие страницы добавления задачи')
    def open_add_task(self):
        browser.open('/tasks/add.html')
        return self

    @allure.step('Ввод названия задачи')
    def fill_task_name(self, name_task):
        browser.element('[name="name"]').type(name_task)
        return self

    @allure.step('Ввод описания задачи')
    def fill_task_desc(self, desc_task):
        browser.element('textarea[name="description"]').type(desc_task)
        return self

    @allure.step('Нажатие на кнопку Добавить задачу')
    def click_add_task(self):
        browser.element('[value="Добавить задачу"]').click()
        return self

    @allure.step('Добавление задачи')
    def add_task(self, task: Task):
        self.fill_task_name(task.name_task).fill_task_desc(task.desc_task).click_add_task()

    @allure.step('Проверка добавления задачи')
    def check_add_task(self, task: Task):
        rows = browser.all('table.table')
        for row in rows:
            name = row.element('ins').get(query.text).strip()
            assert task.name_task in name, f'Expected name "{task.name_task}", but got "{name}"'
        return self


add_task = AddTask()
