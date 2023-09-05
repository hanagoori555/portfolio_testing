from demoqa.pages.classBasePage import BasePage
from demoqa.components.components import WebElement


class HomePage(BasePage):
    def __init__(self, driver):
        self.base_url = "https://www.saucedemo.com"
        super().__init__(driver, self.base_url)

        self.text_login = WebElement(driver=driver,
                                     locator="#login_credentials")
        self.text_password = WebElement(driver=driver,
                                        locator="div.login_password")
