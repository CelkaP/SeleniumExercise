from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import (
    Options,
)  # Import Options for configuring Chrome
from webdriver_manager.chrome import ChromeDriverManager

WEBSITE_URL = "https://blog.griddynamics.com"


def web_driver_setup():
    """
    Setup Selenium web driver and open Chrome browser in headless mode.
    :return: Selenium web driver
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Enable headless mode
    chrome_options.add_argument("--window-size=1500x1240")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )
    driver.set_window_size(1500,1240)

    driver.get(WEBSITE_URL)

    return driver
