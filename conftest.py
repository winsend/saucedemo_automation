import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from allure_commons.types import AttachmentType


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        try:
            driver = item.funcargs.get("driver")
            if driver:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="Скриншот ошибки",
                    attachment_type=AttachmentType.PNG
                )
        except Exception as e:
            print(f"Не удалось сделать скриншот: {e}")