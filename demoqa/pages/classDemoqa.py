from demoqa.pages.classBagePage import BasePage
from demoqa.components.components import WebElement


class Demoqa(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/"
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, "#app > header > a")
        self.button_elements = WebElement(driver, "#app > div > div > div.home-body > div > div:nth-child(1)")
