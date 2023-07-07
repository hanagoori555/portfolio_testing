import time

from demoqa.pages.classBagePage import BasePage
from selenium.common.exceptions import NoSuchElementException


class Demoqa(BasePage):
    def exist_icon(self):
        try:
            self.find_element(locator="#app > header > a")
        except NoSuchElementException:
            return False
        return True

    def click_on_the_icon(self):
        time.sleep(5)
        return self.find_element(locator="#app > header > a").click()
