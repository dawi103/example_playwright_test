from playwright.sync_api import Page, expect

from automation.saucedemo.Pages.InventoryPage import InventoryPage
from automation.saucedemo.Pages.LoginPage import LoginPage


class TestLogout:

    def test_logout(self, page: Page) -> None:
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)
        login_page.go_site()
        login_page.filling_username("standard_user")
        login_page.filling_password("secret_sauce")
        login_page.click_login_button()
        inventory_page.click_burger_button()
        inventory_page.click_logout_button()
        main_page = page.get_by_text("Swag Labs")
        expect(main_page).to_have_text("Swag Labs")
