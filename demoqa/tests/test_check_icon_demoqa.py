from selenium import webdriver
from selenium.webdriver.common.by import By


def test_icon_exist_edge():
    driver = webdriver.Edge()
    driver.get("https://demoqa.com")
    icon = driver.find_element(By.CSS_SELECTOR, "#app > header > a")

    if icon is None:
        print("Element not found")
    else:
        print("Element found")


def test_icon_exist_yandex():
    chrome_options = webdriver.ChromeOptions()
    # link for YandexBrowser
    chrome_options.binary_location = r"C:\Users\Toha\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
    # link for chromedriver (Yandex: 112.0.5615.674)
    chrome_driver = r"C:\Users\Toha\PycharmProjects\portfolio_testing\demoqa\tests\applications\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    driver.get("https://demoqa.com")

    icon = driver.find_element(By.CSS_SELECTOR, "#app > header > a")

    if icon is None:
        print("Element not found")
    else:
        print("Element found")
