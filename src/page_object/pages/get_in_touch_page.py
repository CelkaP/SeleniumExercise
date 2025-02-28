import selenium.common
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from src.page_object.locators import Locator
from src.page_object.pages.blog_page import BlogPage


class GetInTouchPage:
    def __init__(self, driver):
        self.__driver = driver

    @property
    def first_name(self):
        return self.__driver.find_element(By.XPATH, Locator.first_name)

    @property
    def last_name(self):
        return self.__driver.find_element(By.XPATH, Locator.last_name)

    @property
    def email(self):
        return self.__driver.find_element(By.XPATH, Locator.email)

    @property
    def interested_in(self):
        return self.__driver.find_element(By.XPATH, Locator.interested_in)

    @property
    def careers_employment(self):
        return self.__driver.find_element(By.XPATH, Locator.careers_employment)

    @property
    def terms_checkbox(self):
        return self.__driver.find_element(By.XPATH, Locator.terms_checkbox)

    @property
    def newsletter(self):
        return self.__driver.find_element(By.XPATH, Locator.newsletter)

    @property
    def submit_btn(self):
        return self.__driver.find_element(By.XPATH, Locator.submit_btn)

    @property
    def submit_btn_class(self):
        return self.submit_btn.get_attribute("class")

    @property
    def accept_cookies_button(self):
        return self.__driver.find_element(By.XPATH, Locator.cookies_agree_button)

    def click_accept_cookies_button(self):
        if ec.presence_of_element_located(
            self.accept_cookies_button
        ) and ec.element_to_be_clickable(self.accept_cookies_button):
            self.accept_cookies_button.click()

    def enter_first_name(self, first_name):
        self.first_name.send_keys(first_name)

    def enter_last_name(self, last_name):
        self.last_name.send_keys(last_name)

    def enter_email(self, email):
        self.email.send_keys(email)

    def click_interested_in(self):
        try:
            self.interested_in.click()
        except selenium.common.ElementClickInterceptedException as e:
            self.click_accept_cookies_button()
            self.interested_in.click()

    def click_careers_employment(self):
        self.careers_employment.click()

    def accept_terms(self):
        if not self.terms_checkbox.is_selected():
            self.terms_checkbox.click()

    def accept_newsletter(self):
        if not self.newsletter.is_selected():
            self.newsletter.click()
