import selenium.common
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from src.page_object.locators import Locator


class LeadershipPage:
    def __init__(self, driver):
        self.__driver = driver
        WebDriverWait(self.__driver, 2)

    @property
    def leonard(self):
        WebDriverWait(self.__driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, Locator.leonard))
        )
        return self.__driver.find_element(By.XPATH, Locator.leonard)

    @property
    def leonard_position(self):
        WebDriverWait(self.__driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Locator.leonard_position))
        )
        return self.__driver.find_element(By.XPATH, Locator.leonard_position).text

    @property
    def leonard_bio(self):
        WebDriverWait(self.__driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Locator.leonard_bio))
        )
        return self.__driver.find_element(By.XPATH, Locator.leonard_bio).text

    def click_on_leonard(self):
        try:
            self.leonard.click()
        except selenium.common.exceptions.ElementNotInteractableException as e:
            ActionChains(self.__driver).move_to_element(self.leonard).click(
                self.leonard
            ).perform()
