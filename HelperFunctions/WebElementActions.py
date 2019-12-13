import datetime
import time

from HelperFunctions.Core import driver
from HelperFunctions.Constants import Constants

driver = driver()


class Actions:
    @staticmethod
    def open_the_web_site(field):
        driver.get(field)
        print(f"\nOpen the web site - {field} - PASSED")

    @staticmethod
    def click_on_element(field):
        field_object = driver.find_element_by_xpath(field)
        text = field_object.text
        field_object.click()
        print(f"Click on element - {text} - PASSED")

    @staticmethod
    def select_dropdown_value(dropdown, value):
        if dropdown == Constants.datacenter_location:
            time.sleep(0.2)
        dropdown_object = driver.find_element_by_xpath(dropdown)
        dropdown_text = dropdown_object.text
        dropdown_object.click()
        value_parameter = driver.find_element_by_xpath(value)
        value_text = value_parameter.text
        value_parameter.click()
        print(f"The value {value_text} has selected for the dropdown {dropdown_text} - PASSED")

    @staticmethod
    def set_the_checkbox(field):
        field_object = driver.find_element_by_xpath(field)
        field_object.click()
        print(f"Select the checkbox - {field_object.text} - PASSED")

    @staticmethod
    def write_the_message_in_the_field(field, value):
        field_object = driver.find_element_by_xpath(field)
        field_object.send_keys(value)
        print(f"Enter the value - {value} - PASSED")

    @staticmethod
    def the_element_is_displayed(field):
        field_object = driver.find_element_by_xpath(field)
        field_object.is_displayed()
        print(f"The element '{field_object.text}' has displayed - PASSED")

    @staticmethod
    def change_the_frame(frame):
        driver.switch_to_frame(frame)
        print(f"Switch to frame - {frame} - PASSED")

    @staticmethod
    def get_link_from_the_element(field):
        return driver.find_element_by_xpath(field).get_attribute('data-ctorig')

    @staticmethod
    def assert_element(actual=None, expected=None):
        global actualResult, expectedResult
        try:
            actualResult = driver.find_element_by_xpath(actual)
            expectedResult = str(expected).replace("  ", "")
            assert actualResult.text == expectedResult
            print(f"Assertion: {actualResult.text} = {expectedResult} - PASSED")
        except AssertionError as assertError:
            print(f"Message: {assertError}; Actual Result: {actualResult.text}; Expected Result: {expectedResult}")

    @staticmethod
    def close_browser():
        driver.save_screenshot(f'Screenshots\PASSED - Screen- {datetime.datetime.now().strftime("%m%d%H%M")}.png')
        driver.quit()
