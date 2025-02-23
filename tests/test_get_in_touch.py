import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from src.main import get_in_touch
from src.setup import setup_driver
import pytest


WEBSITE_URL = "https://blog.griddynamics.com"


@pytest.fixture(scope="module")
def get_submit_button_class():
    """Fixture to set up WebDriver and return submit button class."""
    driver = setup_driver(WEBSITE_URL)
    submit_btn_class = get_in_touch(driver)
    yield submit_btn_class
    driver.quit()


def test_submit_btn_inactive(get_submit_button_class):
    """Check if submit button is disabled"""
    assert get_submit_button_class == "get-in-touch-form__field submit disabled"
