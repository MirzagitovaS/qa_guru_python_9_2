import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_configs():
    browser.config.window_width = 1600
    browser.config.window_height = 1000
    browser.config.browser_name = 'chrome'
    yield
    browser.quit()