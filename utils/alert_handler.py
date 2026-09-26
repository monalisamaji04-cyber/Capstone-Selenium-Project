from selenium.common.exceptions import NoAlertPresentException


def handle_alert(driver):

    try:

        alert = driver.switch_to.alert

        print("Alert found:", alert.text)

        alert.accept()

        print("Alert accepted.")

    except NoAlertPresentException:

        print("No alert present.")