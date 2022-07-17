import allure
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


def test_github_with_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.MINOR)
    allure.dynamic.feature('Вкладка Issues')
    allure.dynamic.story('В списке Issues есть №76')
    allure.dynamic.link('https://github.com', name='Testing')

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


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'A. Prudnikova')
@allure.feature('Вкладка Issues')
@allure.story('В списке Issues есть №76')
@allure.link('https://github.com', name='Testing')
def test_github_with_decorator_labels():

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