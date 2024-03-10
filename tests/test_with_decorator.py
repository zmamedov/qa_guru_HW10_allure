import allure
from selene import browser, by, be


@allure.step("Открыть главную страницу GitHub")
def open_browser():
    browser.open('/')


@allure.step("Поиск репозитория {repo}")
def search_for_repository(repo):
    browser.element('.search-input').click()
    browser.element('.FormControl-input').type(repo).press_enter()


@allure.step("Переход по ссылке репозитория")
def go_to_repository():
    browser.element(by.text('HW10')).click()


@allure.step("Нажать на вкладку 'Issues'")
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step("Проверка issue с номером #{number}")
def should_see_issue_with_number(number):
    browser.element(by.partial_text('#' + number)).should(be.visible)


def test_decorator_github_issue():
    open_browser()
    search_for_repository('zmamedov/qa_guru_HW10_allure')
    go_to_repository()
    open_issue_tab()
    should_see_issue_with_number('3')
