import pytest
from src.page_object.pages.blog_page import BlogPage
from src.page_object.pages.leadership_page import LeadershipPage
from src.test_base.web_driver_setup import web_driver_setup


@pytest.fixture(scope="module")
def driver():
    driver = web_driver_setup()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def cached_bio(driver):
    bp = BlogPage(driver)
    bp.click_leadership_link()
    lp = LeadershipPage(driver)
    lp.click_on_leonard()
    return lp.leonard_bio


@pytest.mark.parametrize("text_to_find", [
    "board of directors since 2006",
    "chief executive officer of grid dynamics"
])
def test_leonard_bio(cached_bio, text_to_find):
    print(f"--------------------\n{cached_bio}\n--------------------")
    assert (
        text_to_find in cached_bio.lower()
    ), f"{text_to_find} not found in bio: \n {cached_bio}"


def test_is_leonard_position_correct(driver):
    bp = BlogPage(driver)
    bp.click_accept_cookies_button()
    bp.click_leadership_link()
    lp = LeadershipPage(driver)
    lp.click_on_leonard()

    assert lp.leonard_position == "CHIEF EXECUTIVE OFFICER AND DIRECTOR"