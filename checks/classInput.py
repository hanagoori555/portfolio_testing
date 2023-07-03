from classCheck import Check


class Input(Check):
    def __init__(self, locator):
        self.locator = locator
        super(Input, self).__init__(self.locator)


search = Input('input#search')
print(search.check_text())
