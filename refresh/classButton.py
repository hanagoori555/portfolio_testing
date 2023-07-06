class Button:
    def __init__(self, text, link, locator):
        self.text = text
        self.link = link
        self.locator = locator

    def click(self):
        return f"You pushed a button, here is its locator: {self.locator}"


menu_btn = Button("Menu", "/menu", "html>div>button#menu")
print(menu_btn.click())
