import selenium.common
from selenium.webdriver.common.by import By
from src.page_object.locators import Locator


class LeadershipPage:
    def __init__(self, driver):
        self.__driver = driver
        self.__leonard_bio = ""

    @property
    def leonard(self):
        return self.__driver.find_element(By.XPATH, Locator.leonard)

    @property
    def leonard_position(self):
        return self.__driver.find_element(By.XPATH, Locator.leonard_position).text

    @property
    def leonard_bio(self):
        bio_texts = []
        for i in range(1, 4):
            try:
                bio_text = self.__driver.find_element(
                    By.XPATH, Locator.leonard_bio + f"[{i}]"
                ).text
                bio_texts.append(bio_text)
            except selenium.common.exceptions.NoSuchElementException:
                break
        return " ".join(bio_texts)

    def click_on_leonard(self):
        self.leonard.click()
