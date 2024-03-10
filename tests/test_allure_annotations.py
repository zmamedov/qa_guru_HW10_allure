import allure
from allure_commons.types import Severity
from selene import browser, by, be


@allure.title("Просмотр issue в репозитории")
@allure.description("Открытие репозитория, поиск issue под номером 3.")
@allure.suite("tests")
@allure.id("1004")
@allure.sub_suite("test_allure_annotations")
@allure.issue("issue")
@allure.testcase("testcase")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "zmamedov")
@allure.feature("Issues в репозитории")
@allure.story("Просмотр Issues в репозитории")
@allure.link("https://github.com", name="Testing")
def test_issue_on_github_with_annotations():
    browser.open('/')

    browser.element('.search-input').click()
    browser.element('.FormControl-input').type('zmamedov/qa_guru_HW10_allure').press_enter()
    browser.element(by.text('HW10')).click()
    browser.element('#issues-tab').click()

    browser.element(by.partial_text('#3')).should(be.visible)
