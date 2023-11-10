class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.burger_button = page.get_by_role("button", name="Open Menu")
        self.logout_button = page.get_by_role("link", name="Logout")



    def click_burger_button(self):
        self.burger_button.click()

    def click_logout_button(self):
        self.logout_button.click()


