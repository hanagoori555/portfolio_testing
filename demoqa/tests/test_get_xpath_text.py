from demoqa.pages.classHomePage import HomePage


def test_get_xpath_text(browser):
    home_page = HomePage(browser)
    home_page.visit()
    login = home_page.text_login.get_xpath_text(property_path="childNodes[1].data")
    password = home_page.text_password.get_xpath_text(property_path="childNodes[1].data")
    print(login, password)
