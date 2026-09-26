from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_cart(self):

        cart = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "cart-total")
            )
        )

        cart.click()

    def update_quantity(self, quantity):

        quantity_box = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input[name^='quantity']")
            )
        )

        quantity_box.clear()
        quantity_box.send_keys(str(quantity))

        update_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[data-original-title='Update']")
            )
        )

        update_button.click()

    def get_product_name(self):

        product = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".table-responsive td:nth-child(2) a")
            )
        )

        return product.text

    def get_quantity(self):

        quantity_box = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input[name^='quantity']")
            )
        )

        return quantity_box.get_attribute("value")

    def get_cart_total(self):

        total = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".table-responsive .text-right")
            )
        )

        return total.text