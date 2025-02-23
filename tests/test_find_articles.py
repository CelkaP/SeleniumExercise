import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from src.main import find_articles
from src.setup import setup_driver
import pytest


WEBSITE_URL = "https://blog.griddynamics.com"


@pytest.fixture(scope="module")
def articles_data():
    """Fixture to set up WebDriver and return article data."""
    driver = setup_driver(WEBSITE_URL)
    result_data = find_articles(driver)
    yield result_data
    driver.quit()


def test_is_category_selected(articles_data):
    """Check if the categories are visible."""
    assert articles_data["selected_category"] == "blog-page__filter-select active"


def test_is_filter_selected(articles_data):
    """Check if the cloud and dev-ops filter is selected."""
    assert articles_data["selected_filter_class"] == "sub-category-item selected"


def test_more_than_1_article_filtered(articles_data):
    """Ensure more than one article is present after filtering."""
    assert len(articles_data["articles"]) > 1


def test_is_unfiltered(articles_data):
    """Check if 'All Topics' is selected after resetting the filter."""
    assert articles_data["selected_all_topics_class"] == "sub-category-item selected"


def test_more_than_1_article_unfiltered(articles_data):
    """Ensure more than one article is present after unfiltering."""
    assert len(articles_data["top_articles"]) > 1


def test_different_articles(articles_data):
    """Ensure that filtered and unfiltered articles are not the same."""
    assert articles_data["top_articles"][0] != articles_data["articles"][0]
