import time

from demoqa.pages.classElementsPage import ElementsPage
from demoqa.pages.classAccordian import Accordian


def test_visible_button_sidebar(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    time.sleep(3)
    assert elements_page.button_sidebar_first_textbox.visible()


def test_not_visible_button_sidebar(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.button_sidebar_first_checkbox.visible()
    elements_page.button_sidebar_first.click()
    time.sleep(3)
    assert elements_page.button_sidebar_first_checkbox.not_visible()


def test_visible_accordian(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()
    assert accordian_page.one_paragraph.visible()
    accordian_page.one_section_button.click()
    time.sleep(3)
    assert accordian_page.one_paragraph.not_visible()
