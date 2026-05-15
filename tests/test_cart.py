from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_product_to_cart(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    assert "cart.html" in driver.current_url