from selene import browser, have
import allure


class ProfilePage:

    @allure.step('Открытие сайта')
    def open(self):
        browser.open('')
        return self

    @allure.step('Нажатие на кнопку Посмотреть')
    def click_show_button(self):
        browser.element('.btn-success').click()
        return self

    @allure.step('Проверка страницы профайла')
    def check_profile(self):
        browser.element('h2').should(have.text('Профиль пользователя'))


profile_user_page = ProfilePage()
