from selene import browser, by, be


def test_issue_on_github():
    browser.open('/')

    browser.element('.search-input').click()
    browser.element('.FormControl-input').type('zmamedov/qa_guru_HW10_allure').press_enter()
    browser.element(by.text('HW10')).click()
    browser.element('#issues-tab').click()

    browser.element(by.partial_text('#3')).should(be.visible)
