import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Edge()
    yield driver
    driver.set_window_size(width=1000, height=1000)
    driver.quit()
