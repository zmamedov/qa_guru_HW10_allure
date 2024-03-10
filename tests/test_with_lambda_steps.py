import allure
from selene import browser, by, be


def test_lambda_githab_issue():
    with allure.step("Открыть главную страницу GitHub"):
        browser.open('/')

    with allure.step("Нажать на поле ввода"):
        browser.element('.search-input').click()

    with allure.step("Поиск репозитория 'zmamedov/qa_guru_HW10_allure'"):
        browser.element('.FormControl-input').type('zmamedov/qa_guru_HW10_allure').press_enter()
        browser.element(by.text('HW10')).click()

    with allure.step("Нажать на вкладку 'Issues'"):
        browser.element('#issues-tab').click()

    with allure.step("Проверка issue с номером #3"):
        browser.element(by.partial_text('#3')).should(be.visible)
