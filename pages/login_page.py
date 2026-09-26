from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def enter_email(self, email):

        element = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "input-email")
            )
        )

        element.clear()
        element.send_keys(email)

    def enter_password(self, password):

        element = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "input-password")
            )
        )

        element.clear()
        element.send_keys(password)

    def click_login(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input[type='submit']")
            )
        )

        element.click()

    def login(self, email, password):

        self.enter_email(email)
        self.enter_password(password)
        self.click_login()