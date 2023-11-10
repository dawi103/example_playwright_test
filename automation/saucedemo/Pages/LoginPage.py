class LoginPage:
    def __init__(self, page):
        self.page = page
        self.fill_username = page.locator("[data-test=\"username\"]")
        self.fill_password = page.locator("[data-test=\"password\"]")
        self.click_button = page.locator("[data-test=\"login-button\"]")
        self.burger_button = page.get_by_role("button", name="Open Menu")
        self.logout_button = page.get_by_role("link", name="Logout")


    def go_site(self):
        self.page.goto("https://www.saucedemo.com/")


    def filling_password(self, password):
        self.fill_password.fill(password)


    def filling_username(self, username):
        self.fill_username.fill(username)

    def click_login_button(self):
        self.click_button.click()

