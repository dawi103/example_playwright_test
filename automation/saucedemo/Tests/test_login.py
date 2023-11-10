from playwright.sync_api import Page, expect

from automation.saucedemo.Pages.LoginPage import LoginPage


class TestLogin:

    def test_login_with_correct_data(self, page: Page) -> None:
        login_page = LoginPage(page)
        login_page.go_site()
        login_page.filling_username("standard_user")
        login_page.filling_password("secret_sauce")
        login_page.click_login_button()
        title = page.get_by_text('Products')
        expect(title).to_contain_text('Products')


    def test_login_with_invalid_data(self, page: Page) -> None:
        login_page = LoginPage(page)
        login_page.go_site()
        login_page.filling_username("stranger_user")
        login_page.filling_password("secret_sauce")
        login_page.click_login_button()
        error_message = page.get_by_text("Epic sadface: Username and password do not match any user in this service")
        expect(error_message).to_have_text("Epic sadface: Username and password do not match any user in this service")



    def test_login_without_data(self, page: Page) -> None:
        login_page = LoginPage(page)
        login_page.go_site()
        login_page.click_login_button()
        expected_message = "Epic sadface: Username is required"
        error_message = page.get_by_text(expected_message)
        expect(error_message).to_contain_text(expected_message)


    def test_with_only_user(self, page: Page) -> None:
        login_page = LoginPage(page)
        login_page.go_site()
        login_page.filling_username("standard_user")
        login_page.click_login_button()
        expected_message = "Epic sadface: Password is required"
        error_message = page.get_by_text("Epic sadface: Password is required")
        expect(error_message).to_contain_text(expected_message)
