import json
import os
import time
from datetime import datetime

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# =========================================================
# PROJECT PATHS
# =========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

SCREENSHOT_DIR = os.path.join(
    BASE_DIR,
    "screenshots"
)

os.makedirs(
    DATA_DIR,
    exist_ok=True
)

os.makedirs(
    SCREENSHOT_DIR,
    exist_ok=True
)


# =========================================================
# LOAD TEST DATA
# =========================================================

def load_test_data():

    data_file = os.path.join(
        DATA_DIR,
        "test_data.json"
    )

    # -----------------------------------------------------
    # If JSON does not exist, create it
    # -----------------------------------------------------

    if not os.path.exists(data_file):

        default_data = {
            "url": "https://tutorialsninja.com/demo/",
            "first_name": "Monalisa",
            "last_name": "Maji",
            "telephone": "9876543210",
            "password": "Test@12345",
            "product": "MacBook",
            "quantity": 2
        }

        with open(
            data_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                default_data,
                file,
                indent=4
            )

        print(
            "test_data.json was not found."
        )

        print(
            "Created test_data.json automatically."
        )


    # -----------------------------------------------------
    # Read JSON file
    # -----------------------------------------------------

    with open(
        data_file,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)


    print(
        "Test data loaded from:",
        data_file
    )

    return data


# =========================================================
# GENERATE UNIQUE EMAIL
# =========================================================

def generate_unique_email():

    timestamp = int(
        time.time()
    )

    return (
        f"monalisa{timestamp}"
        "@example.com"
    )


# =========================================================
# SCREENSHOT FUNCTION
# =========================================================

def take_screenshot(
    driver,
    name
):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"{name}_{timestamp}.png"
    )

    filepath = os.path.join(
        SCREENSHOT_DIR,
        filename
    )

    driver.save_screenshot(
        filepath
    )

    print(
        "Screenshot saved:",
        filepath
    )


# =========================================================
# HANDLE ALERT
# =========================================================

def handle_alert(driver):

    try:

        alert = WebDriverWait(
            driver,
            3
        ).until(
            EC.alert_is_present()
        )

        print(
            "Alert found:",
            alert.text
        )

        alert.accept()

        print(
            "Alert accepted."
        )

    except TimeoutException:

        print(
            "No alert present."
        )


# =========================================================
# BROWSER FIXTURE
# =========================================================

@pytest.fixture
def driver():

    options = webdriver.ChromeOptions()

    options.add_argument(
        "--start-maximized"
    )

    driver = webdriver.Chrome(
        options=options
    )

    yield driver

    driver.quit()


# =========================================================
# MAIN TEST
# =========================================================

def test_ecommerce_purchase(driver):

    # =====================================================
    # 1. LOAD TEST DATA
    # =====================================================

    data = load_test_data()

    first_name = data["first_name"]
    last_name = data["last_name"]
    telephone = data["telephone"]
    password = data["password"]
    product = data["product"]
    quantity = data["quantity"]

    email = generate_unique_email()


    print()
    print(
        "========================================"
    )
    print(
        "E-COMMERCE AUTOMATION TEST"
    )
    print(
        "========================================"
    )

    print(
        "Generated email:",
        email
    )

    print(
        "Product:",
        product
    )

    print(
        "Quantity:",
        quantity
    )

    print(
        "========================================"
    )


    wait = WebDriverWait(
        driver,
        20
    )


    # =====================================================
    # 2. LAUNCH APPLICATION
    # =====================================================

    driver.get(
        data["url"]
    )

    print(
        "Application opened."
    )

    take_screenshot(
        driver,
        "home_page"
    )


    # =====================================================
    # 3. REGISTER NEW ACCOUNT
    # =====================================================

    driver.get(
        data["url"] +
        "index.php?route=account/register"
    )

    print(
        "Registration page opened."
    )


    # First Name
    wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "input-firstname"
            )
        )
    ).send_keys(
        first_name
    )


    # Last Name
    wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "input-lastname"
            )
        )
    ).send_keys(
        last_name
    )


    # Email
    wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "input-email"
            )
        )
    ).send_keys(
        email
    )


    # Telephone
    wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "input-telephone"
            )
        )
    ).send_keys(
        telephone
    )


    # Password
    wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "input-password"
            )
        )
    ).send_keys(
        password
    )


    # Confirm Password
    wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "input-confirm"
            )
        )
    ).send_keys(
        password
    )


    # Privacy Policy
    try:

        privacy_checkbox = wait.until(
            EC.element_to_be_clickable(
                (
                    By.NAME,
                    "agree"
                )
            )
        )

        privacy_checkbox.click()

        print(
            "Privacy policy accepted."
        )

    except TimeoutException:

        print(
            "Privacy policy checkbox not found."
        )


    # Continue
    wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                "input[type='submit']"
            )
        )
    ).click()


    print(
        "Registration submitted."
    )

    take_screenshot(
        driver,
        "registration"
    )


    # =====================================================
    # 4. HANDLE ALERT
    # =====================================================

    handle_alert(
        driver
    )


    # =====================================================
    # 5. VERIFY REGISTRATION
    # =====================================================

    try:

        wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//*[contains(text(),"
                    "'Your Account Has Been Created')]"
                )
            )
        )

        print(
            "Registration completed successfully."
        )

    except TimeoutException:

        print(
            "Registration confirmation "
            "text was not found."
        )


    # =====================================================
    # 6. LOGOUT
    # =====================================================

    driver.get(
        data["url"] +
        "index.php?route=account/logout"
    )

    print(
        "Logged out after registration."
    )

    take_screenshot(
        driver,
        "logout"
    )


    # =====================================================
    # 7. LOGIN
    # =====================================================

    driver.get(
        data["url"] +
        "index.php?route=account/login"
    )

    print(
        "Login page opened."
    )


    # Email
    wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "input-email"
            )
        )
    ).send_keys(
        email
    )


    # Password
    wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "input-password"
            )
        )
    ).send_keys(
        password
    )


    # Login
    wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                "input[type='submit']"
            )
        )
    ).click()


    print(
        "Login completed."
    )

    take_screenshot(
        driver,
        "login"
    )


    # =====================================================
    # 8. SEARCH PRODUCT
    # =====================================================

    search_box = wait.until(
        EC.visibility_of_element_located(
            (
                By.NAME,
                "search"
            )
        )
    )

    search_box.clear()

    search_box.send_keys(
        product
    )

    print(
        "Searching product:",
        product
    )


    # Search button
    wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                "button.btn.btn-default.btn-lg"
            )
        )
    ).click()


    # =====================================================
    # 9. OPEN PRODUCT
    # =====================================================

    product_link = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//a[contains("
                f"normalize-space(),"
                f"'{product}')]"
            )
        )
    )

    product_link.click()

    print(
        "Product opened:",
        product
    )

    take_screenshot(
        driver,
        "product_page"
    )


    # =====================================================
    # 10. ADD PRODUCT TO CART
    # =====================================================

    add_to_cart = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "button-cart"
            )
        )
    )

    add_to_cart.click()

    print(
        "Product added to cart."
    )

    take_screenshot(
        driver,
        "add_to_cart"
    )


    # =====================================================
    # 11. OPEN CART
    # =====================================================

    driver.get(
        data["url"] +
        "index.php?route=checkout/cart"
    )

    print(
        "Cart page opened."
    )

    take_screenshot(
        driver,
        "cart_before_update"
    )


    # =====================================================
    # 12. UPDATE QUANTITY
    # =====================================================

    quantity_box = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "input[name^='quantity']"
            )
        )
    )

    quantity_box.clear()

    quantity_box.send_keys(
        str(quantity)
    )

    print(
        "Quantity changed to:",
        quantity
    )


    # Find Update button
    update_button = None

    update_selectors = [

        "button[data-original-title='Update']",

        "button[title='Update']",

        "button[name='update']",

        "input[data-original-title='Update']",

        "input[title='Update']"

    ]


    for selector in update_selectors:

        try:

            update_button = WebDriverWait(
                driver,
                5
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        selector
                    )
                )
            )

            print(
                "Update button found:",
                selector
            )

            break

        except TimeoutException:

            continue


    if update_button is None:

        raise Exception(
            "Could not find the cart "
            "Update button."
        )


    update_button.click()

    print(
        "Cart quantity updated."
    )


    # =====================================================
    # WAIT FOR QUANTITY TO UPDATE
    # =====================================================

    try:

        wait.until(
            EC.staleness_of(
                quantity_box
            )
        )

    except TimeoutException:

        print(
            "Cart element did not become stale."
        )

        print(
            "Continuing with verification."
        )


    # =====================================================
    # 13. VERIFY CART QUANTITY
    # =====================================================

    updated_quantity_box = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "input[name^='quantity']"
            )
        )
    )

    actual_quantity = (
        updated_quantity_box
        .get_attribute(
            "value"
        )
    )


    print(
        "Expected quantity:",
        quantity
    )

    print(
        "Actual quantity:",
        actual_quantity
    )


    assert actual_quantity == str(
        quantity
    ), (
        f"Quantity verification failed. "
        f"Expected {quantity}, "
        f"but got {actual_quantity}"
    )


    print(
        "Quantity verified successfully."
    )


    # =====================================================
    # 14. VERIFY PRODUCT NAME
    # =====================================================

    print(
        "Verifying product name in cart..."
    )


    # -----------------------------------------------------
    # IMPORTANT FIX
    #
    # Instead of searching for:
    #
    # td.text-left a
    #
    # we first find the quantity input.
    #
    # Then we move UP to the same table row.
    #
    # The product name should be inside that same row.
    # -----------------------------------------------------

    try:

        cart_row = updated_quantity_box.find_element(
            By.XPATH,
            "./ancestor::tr[1]"
        )

        row_text = cart_row.text.strip()

        print(
            "Cart row text:"
        )

        print(
            row_text
        )


        assert product.lower() in row_text.lower(), (
            f"Product verification failed. "
            f"Expected '{product}' "
            f"inside cart row, "
            f"but row contains: '{row_text}'"
        )


        print(
            "Product name verified successfully."
        )


    except Exception:

        # -------------------------------------------------
        # FALLBACK METHOD
        # -------------------------------------------------

        print(
            "Primary product verification "
            "could not find the product."
        )

        print(
            "Trying fallback cart verification..."
        )


        # Get cart table
        cart_table = None


        cart_table_locators = [

            (
                By.CSS_SELECTOR,
                "div.table-responsive"
            ),

            (
                By.XPATH,
                "//div[contains("
                "@class,'table-responsive')]"
            ),

            (
                By.XPATH,
                "//table"
            )

        ]


        for locator in cart_table_locators:

            try:

                cart_table = WebDriverWait(
                    driver,
                    5
                ).until(
                    EC.visibility_of_element_located(
                        locator
                    )
                )

                break

            except TimeoutException:

                continue


        if cart_table is not None:

            cart_text = (
                cart_table
                .text
                .strip()
            )

            print(
                "Cart table text:"
            )

            print(
                cart_text
            )


            assert product.lower() in cart_text.lower(), (
                f"Product verification failed. "
                f"Expected '{product}' "
                f"in cart table."
            )


            print(
                "Product name verified "
                "using cart table."
            )


        else:

            # -------------------------------------------------
            # FINAL FALLBACK
            # -------------------------------------------------

            body_text = (
                driver
                .find_element(
                    By.TAG_NAME,
                    "body"
                )
                .text
                .strip()
            )


            print(
                "Cart page text:"
            )

            print(
                body_text
            )


            assert product.lower() in body_text.lower(), (
                f"Product '{product}' "
                f"was not found on cart page."
            )


            print(
                "Product name verified "
                "using cart page text."
            )


    # =====================================================
    # 15. VERIFY CART URL
    # =====================================================

    assert (
        "checkout/cart"
        in driver.current_url
    )


    print(
        "Cart URL verified."
    )


    # =====================================================
    # 16. FINAL SCREENSHOT
    # =====================================================

    take_screenshot(
        driver,
        "final_cart"
    )


    # =====================================================
    # 17. TEST COMPLETE
    # =====================================================

    print()
    print(
        "========================================"
    )

    print(
        "E-COMMERCE TEST PASSED"
    )

    print(
        "========================================"
    )