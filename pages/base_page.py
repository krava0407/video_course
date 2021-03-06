from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        self.go_to_element(self.element_is_present(locator))
        return wait(driver=self.driver, timeout=timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=15):
        return wait(driver=self.driver, timeout=timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(driver=self.driver, timeout=timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=5):
        return wait(driver=self.driver, timeout=timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(driver=self.driver, timeout=timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5.2):
        return wait(driver=self.driver, timeout=timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   element)  # """execute_script - метод который позволяет запускать скрипты"""

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def close_active_tab(self):
        self.driver.close()

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('fixedban').remove();")
        #"amp-animate amp-mode-mouse"


