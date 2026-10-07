import time

from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=5):
        return self.driver.find_element(*locator)
        # deadline = time.time() + timeout
        # last_error = None
        #
        # while time.time() < deadline:
        #     try:
        #         return self.driver.find_element(*locator)
        #     except (NoSuchElementException, StaleElementReferenceException) as exc:
        #         last_error = exc
        #         time.sleep(0.2)
        #
        # raise last_error

    # def click(self, locator):
    #     self.find(locator).click()
    #
    # def fill(self, locator, value):
    #   element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
    #   element.clear()
    #   element.send_keys(value)

    def click(self, locator):
        # logger.info(f"Click on {locator}")
        # element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        # element.click()
        logger.debug(f"Click on  {locator}")
        self.wait_until_clickable(locator).click()

    def fill(self, locator, value):
        logger.info(f"Fill{locator}with{value}")
        element = self.wait_until_visible(locator)
        element.clear()
        element.send_keys(value)

        # self.find(locator).clear()
        # self.find(locator).send_keys(value)



    def get_alert_text(self):
        # alert = WebDriverWait(self.driver, timeout=5).until(
        #     EC.alert_is_present()
        # )
        # return alert.text
        return self.wait_until_alert_present().text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def wait_until_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

    def wait_until_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable(locator))

    def wait_until_url_matches(self, locator, timeout=5):
        return WebDriverWait(self.driver,timeout).until(EC.url_matches(locator))

    def wait_until_alert_present(self, timeout=5):
        return WebDriverWait(self.driver,timeout).until(EC.alert_is_present())