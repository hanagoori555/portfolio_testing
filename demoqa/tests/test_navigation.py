from demoqa.pages.classDemoqa import Demoqa
from demoqa.pages.classElementsPage import ElementsPage


def test_navigation(browser):
    demoqa_page = Demoqa(browser)
    elements_page = ElementsPage(browser)

    demoqa_page.visit()
    demoqa_page.button_elements.click()

    elements_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    elements_page.equal_url()
