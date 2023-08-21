from demoqa.pages.classDemoqa import Demoqa
from demoqa.pages.classElementsPage import ElementsPage


def test_check_text_please(browser):
    demoqa_page = Demoqa(browser)
    elements_page = ElementsPage(browser)
    demoqa_page.visit()
    demoqa_page.button_elements.click()
    assert elements_page.text_please.get_text() == "Please select an item from left to start practice."
