import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from src.main import find_leonard_position
from src.setup import setup_driver

WEBSITE_URL = "https://blog.griddynamics.com"


@pytest.fixture(scope="module")
def driver():
    driver = setup_driver(WEBSITE_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def result(driver):
    return find_leonard_position(driver)


def test_leonard_position_correct(result):
    assert result == "Chief Executive Officer and Director"
