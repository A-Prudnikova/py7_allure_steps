import allure
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github():
    with allure.step('Открываем главную страниццу в максимальном размере'):
        browser.open("https://github.com").driver.maximize_window()

    with allure.step('Ищем репозиторий'):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("eroshenkoam/allure-example")
        s(".header-search-input").submit()

    with allure.step('Переходим по ссылке в репозиторий'):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step('Открываем вкладку Issues'):
        s("#issues-tab").click()

    with allure.step('Проверяем наличие Issue с номером 76'):
        s(by.partial_text("#76")).should(be.visible)