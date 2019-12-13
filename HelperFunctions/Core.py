import datetime
import os.path

from selenium import webdriver
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element_by_xpath(value)))

    # def after_find(self, by, value, driver):
    #     value_text = str(driver.find_element_by_xpath(value).text).replace("  ", "")
    #     print(f"{value_text} - PASSED")

    def on_exception(self, exception, driver):
        driver.save_screenshot(f"..\Screenshots\Screen- {datetime.datetime.now().strftime('%m/%d_%H:%M')}.png")
        raise exception


def driver():
    driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    driver.maximize_window()
    driver.implicitly_wait(10)
    # request.addfinalizer(driver.quit)
    return driver


screenshots_folder = "Screenshots"

if not os.path.isdir(screenshots_folder):
    os.mkdir(screenshots_folder)
