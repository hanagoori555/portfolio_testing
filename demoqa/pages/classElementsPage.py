from demoqa.pages.classBasePage import BasePage
from demoqa.components.components import WebElement


class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/elements"
        self.text_please = WebElement(driver,
                                      "#app > div > div > div.row > "
                                      "div.col-12.mt-4.col-md-6")
        self.text_elements = WebElement(
            driver,
            "#app > div > div > "
            "div.pattern-backgound.playgound-header > div")
        self.icon = WebElement(driver, "#app > header > a > img")
        self.button_sidebar_first = WebElement(driver,
                                               "div:nth-child(1) > span > div")
        self.button_sidebar_first_textbox = WebElement(driver,
                                                       "div:nth-child(1) > "
                                                       "div > ul > #item-0 > "
                                                       "span")
        self.button_sidebar_first_checkbox = WebElement(driver,
                                                        "div:nth-child(1) > "
                                                        "div > ul > #item-1 > "
                                                        "span")
        self.buttons_first_menu = WebElement(driver,
                                             "div:nth-child(1) > div > ul > "
                                             "li")
        super().__init__(driver, self.base_url)
