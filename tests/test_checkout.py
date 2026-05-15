from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page.click_checkout()

    checkout_page.fill_information(
        "Vlad",
        "frrrrrr",
        "12345"
    )

    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    assert checkout_page.get_success_text() == "Thank you for your order!"