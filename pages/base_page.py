from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def element_is_visible(self, locator):
        self.scroll_to_element(self.element_is_presence(locator))
        return WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(locator))

    def element_is_presence(self, locator):
        return WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(locator))

    def element_is_clickable(self, locator):
        return WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable(locator))

    def scroll_to_element(self, locator):
        ActionChains(self.driver).scroll_to_element(locator).perform()

    def get_current_url(self, url):
        wait = WebDriverWait(self.driver, timeout=10).until(EC.url_to_be(url))
        if wait is True:
            return self.driver.current_url

    def switch_to_window(self, index_page):
        self.driver.switch_to.window(self.driver.window_handles[index_page])
