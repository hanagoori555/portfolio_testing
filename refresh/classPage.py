from selenium import webdriver


class Page:
    def __init__(self, url):
        self.url = url

    def get(self):
        driver = webdriver.Chrome()
        driver.get(self.url)


important_information = Page("https://devby.io/news/it-memy")
important_information.get()
