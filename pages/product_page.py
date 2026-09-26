from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def search_product(self, product):

        search_box = self.wait.until(
            EC.visibility_of_element_located(
                (By.NAME, "search")
            )
        )

        search_box.clear()
        search_box.send_keys(product)

        search_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")
            )
        )

        search_button.click()

    def open_product(self, product):

        product_link = self.wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, product)
            )
        )

        product_link.click()

    def add_to_cart(self):

        add_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "button-cart")
            )
        )

        add_button.click()