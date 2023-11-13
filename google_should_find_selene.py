from selene.support.shared import browser
from selene import be, have

def test_browser_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_browser_search_invalid_data():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('gzdbdfbdfbdfb').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу gzdbdfbdfbdfb ничего не найдено.'))


