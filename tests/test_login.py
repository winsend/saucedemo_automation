import allure
import pytest

from pages.login_page import LoginPage

@allure.feature("Авторизация")
@allure.story("Успешный логин")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Успешный вход с валидными данными")
@pytest.mark.login
@pytest.mark.parametrize (
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce")
    ]
)

def test_success_login(driver, username, password): 

    login_page = LoginPage(driver)

    with allure.step("Открываем страницу логина"):
        login_page.open_login_page()

    with allure.step(f"Вводим логин {username} и пароль"):
        login_page.login(username, password)

    with allure.step("Проверяем переход на inventory страницу"):
        assert "inventory.html" in driver.current_url


@allure.feature("Авторизация")
@allure.story("Неверный логин или пароль")
@allure.title("Вход с невалидными данными")
@pytest.mark.negative
@pytest.mark.parametrize(
    "username,password",
    [
        ("locked_out_user", "secret_sauce"),
        ("standard_user", "wrong_password"),
        ("", "secret_sauce"),
        ("standard_user", "")
    ]
)

def test_negative_login(driver, username, password):

    login_page = LoginPage(driver)
    with allure.step("Открываем страницу логина"):
        login_page.open_login_page()

    with allure.step(f"Вводим логин {username} и пароль"):
        login_page.login(username, password)

    error_message = login_page.get_error_message()

    with allure.step("Проверяем error_message"):
        assert error_message is not None
