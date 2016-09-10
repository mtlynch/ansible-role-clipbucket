"""Simple automation for ClipBucket web application.

ClipBucketDriver drives a web UI for ClipBucket, using the Selenium WebDriver
API.
"""

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import ui

# Standard timeout (in seconds) to wait for a page element to appear.
TIMEOUT = 5


class Error(Exception):
    pass


class ClipBucketModuleError(Error):
    pass


class ClipBucketDriver(object):

    def __init__(self, base_url):
        self._driver = webdriver.Firefox()
        self._base_url = base_url

    def get(self, relative_url):
        self._driver.get(self._base_url + relative_url)

    def do_login(self, username, password):
        self.get('/admin_area/login.php')

        username_element = self._driver.find_element_by_id('username')
        ui.WebDriverWait(
            self._driver, TIMEOUT).until(
            expected_conditions.visibility_of(username_element))
        password_element = self._driver.find_element_by_id('password')

        username_element.send_keys(username)
        password_element.send_keys(password)
        self._driver.find_element_by_name('login').click()

    def do_check_modules(self):
        self.get('/admin_area/cb_mod_check.php')

        for module_element in self._driver.find_elements_by_class_name('well'):
            try:
                alert_element = module_element.find_element_by_class_name(
                    'alert')
                # Ignore missing Mp4box module for now.
                # https://github.com/mtlynch/ansible-role-clipbucket/issues/24
                if alert_element.text.startswith('Mp4box'):
                  continue
                if alert_element:
                    raise ClipBucketModuleError(alert_element.text)
            except exceptions.NoSuchElementException:
                # Lack of alert is good: the module is installed correctly.
                continue

    def quit(self):
        self._driver.quit()

