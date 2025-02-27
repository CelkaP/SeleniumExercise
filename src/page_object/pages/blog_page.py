import selenium.common
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from src.page_object.locators import Locator
from selenium.webdriver.support import expected_conditions as ec


class BlogPage:
    def __init__(self, driver):
        self.__driver = driver
        WebDriverWait(self.__driver, 2)

    @property
    def accept_cookies_button(self):
        return self.__driver.find_element(By.XPATH, Locator.cookies_agree_button)

    @property
    def leadership(self):
        return self.__driver.find_element(
            By.XPATH, Locator.leadership_under_about
        )

    @property
    def filter_by(self):
        return self.__driver.find_element(By.XPATH, Locator.filter_by)

    @property
    def cloud_and_dev_ops_filter(self):
        return self.__driver.find_element(By.XPATH, Locator.cloud_and_dev_ops_filter)

    @property
    def articles(self):
        return self.__driver.find_elements(By.XPATH, Locator.articles)

    @property
    def all_topics(self):
        return self.__driver.find_elements(By.XPATH, Locator.all_topics)

    @property
    def top_articles(self):
        return self.__driver.find_elements(By.XPATH, Locator.top_articles)

    @property
    def get_in_touch_button(self):
        return self.__driver.find_element(By.XPATH, Locator.get_in_touch_button)

    def click_get_in_touch_button(self):
        self.get_in_touch_button.click()

    def click_accept_cookies_button(self):
        WebDriverWait(self.__driver, 10).until(
            ec.presence_of_element_located((By.XPATH, Locator.cookies_agree_button))
            and ec.element_to_be_clickable((By.XPATH, Locator.cookies_agree_button))
        )
        self.accept_cookies_button.click()

    def click_leadership_link(self):
        try:
            self.leadership.click()
        except selenium.common.exceptions.ElementNotInteractableException as e:
            ActionChains(self.__driver).move_to_element(self.leadership).click(self.leadership).perform()

    def click_filter_by(self):
        self.filter_by.click()

    def click_all_topics(self):
        self.all_topics.click()

    def click_cloud_and_dev_ops_filter(self):
        self.cloud_and_dev_ops_filter.click()

    def get_selected_category(self):
        return self.filter_by.get_attribute("class")

    def get_selected_all_topics_class(self):
        return self.all_topics.get_attribute("class")

    def get_cloud_and_dev_ops_filter_class(self):
        return self.cloud_and_dev_ops_filter.get_attribute("class")
