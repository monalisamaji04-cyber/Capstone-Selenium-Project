from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_first_name(self, first_name):
        element = self.wait.until(
            EC.visibility_of_element_located((By.ID, "input-firstname"))
        )
        element.send_keys(first_name)

    def enter_last_name(self, last_name):
        element = self.wait.until(
            EC.visibility_of_element_located((By.ID, "input-lastname"))
        )
        element.send_keys(last_name)

    def enter_email(self, email):
        element = self.wait.until(
            EC.visibility_of_element_located((By.ID, "input-email"))
        )
        element.send_keys(email)

    def enter_telephone(self, telephone):
        element = self.wait.until(
            EC.visibility_of_element_located((By.ID, "input-telephone"))
        )
        element.send_keys(telephone)

    def enter_password(self, password):
        element = self.wait.until(
            EC.visibility_of_element_located((By.ID, "input-password"))
        )
        element.send_keys(password)

    def enter_confirm_password(self, password):
        element = self.wait.until(
            EC.visibility_of_element_located((By.ID, "input-confirm"))
        )
        element.send_keys(password)

    def agree_privacy_policy(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.NAME, "agree"))
        )
        element.click()

    def click_continue(self):
        element = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input[type='submit']")
            )
        )
        element.click()

    def register(self, first_name, last_name, email, telephone, password):

        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_telephone(telephone)
        self.enter_password(password)
        self.enter_confirm_password(password)
        self.agree_privacy_policy()
        self.click_continue()