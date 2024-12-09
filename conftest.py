
import pytest
from selene import browser


@pytest.fixture(scope='session')
def browser_manag():
    browser.config.base_url = "https://demoqa.com/"
    browser.config.window_width = 1400
    browser.config.window_height = 850
    browser.open('/automation-practice-form')

    yield

    browser.quit()
