from demoqa.pages.classBagePage import BasePage
from demoqa.components.components import WebElement


class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/elements"
        self.text_please = WebElement(driver, "#app > div > div > div.row > div.col-12.mt-4.col-md-6")
        super().__init__(driver, self.base_url)
