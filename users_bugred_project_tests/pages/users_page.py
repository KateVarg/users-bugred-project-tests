from selene import browser, query
from users_bugred_project_tests.data.data_search import SearchUser
import allure


class SearchUsers:

    @allure.step('Открытие сайта')
    def open(self):
        browser.open('')
        return self

    @allure.step('Выбор даты начала периода для поиска')
    def choose_start_date(self, start_day, start_month, start_year):
        date_value = f'{start_year}.{start_month}.{start_day}'
        browser.execute_script(
            f'document.querySelector(".form-control[name=\'date_start\']").value = "{date_value}";'
        )
        return self

    @allure.step('Выбор даты окончания периода для поиска')
    def choose_end_date(self, end_day, end_month, end_year):
        date_value = f'{end_year}.{end_month}.{end_day}'
        browser.execute_script(
            f'document.querySelector(".form-control[name=\'date_end\']").value = "{date_value}";'
        )
        return self

    @allure.step('Ввод имени')
    def fill_name(self, name):
        browser.element('.form-control[name="q"]').type(name)
        return self

    @allure.step('Нажатие на кнопку "Найти"')
    def click_search_button(self):
        browser.element('.btn-submit').click()
        return self

    @allure.step('Поиск пользователя')
    def register(self, user: SearchUser):
        (
            self.choose_start_date(user.start_date_year, user.start_date_month, user.start_date_day)
            .choose_end_date(user.end_date_year, user.end_date_month, user.end_date_day)
            .fill_name(user.name)
            .click_search_button()
        )
        return self

    @allure.step('Проверка результатов поиска')
    def check_search_result(self, user: SearchUser):
        rows = browser.all('table.table tbody.ajax_load_row tr')
        for row in rows:
            fio = row.element('td:nth-of-type(2)').get(query.text).strip()
            assert user.name in fio, f'Expected name "{user.name}", but got "{fio}"'
        return self


user_search = SearchUsers()
