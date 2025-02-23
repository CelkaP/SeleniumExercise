from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def setup_driver(url):
    """
    Setup Selenium web driver and open Chrome browser with provided url.
    :param url: website url
    :return: Selenium web driver
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.set_window_size(1500, 1240)
    driver.get(url)
    return driver
