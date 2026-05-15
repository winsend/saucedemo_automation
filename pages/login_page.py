from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utils.locators import LoginPageLocators

class LoginPage:
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(username)
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()