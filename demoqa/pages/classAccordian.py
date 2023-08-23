from demoqa.pages.classBagePage import BasePage
from demoqa.components.components import WebElement


class Accordian(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/accordian"
        super().__init__(driver, self.base_url)

        self.one_section_button = WebElement(driver, "#section1Heading")
        self.one_paragraph = WebElement(driver, "#section1Content > p")
