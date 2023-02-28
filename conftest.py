import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome('C:/Users/kiril/PycharmProjects/pythonProject9/chromedriver.exe')
    driver.implicitly_wait(10)

    yield driver
    driver.quit()

