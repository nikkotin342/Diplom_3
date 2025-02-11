import pytest
from selenium import webdriver


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        opts = webdriver.FirefoxOptions()
        opts.add_argument("--width=1920")
        opts.add_argument("--height=1024")
        driver = webdriver.Firefox(options=opts)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()