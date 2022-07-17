import allure
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('76')


@allure.step('Открываем главную страниццу в максимальном размере')
def open_main_page():
    browser.open("https://github.com").driver.maximize_window()

@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()

@allure.step("Переходим по ссылке в репозиторий {repo}")
def go_to_repository(repo):
    s(by.link_text("eroshenkoam/allure-example")).click()

@allure.step("Открываем вкладку Issues")
def open_issue_tab():
    s("#issues-tab").click()

@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text("#" + number)).should(be.visible)