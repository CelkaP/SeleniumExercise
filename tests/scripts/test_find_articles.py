import pytest
from src.page_object.pages.blog_page import BlogPage
from src.test_base.web_driver_setup import web_driver_setup


@pytest.fixture(scope="module")
def driver():
    driver = web_driver_setup()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def articles_cache(driver):
    bp = BlogPage(driver)
    bp.click_accept_cookies_button()
    bp.click_filter_by()
    bp.click_cloud_and_dev_ops_filter()
    cloud_and_dev_ops_articles = bp.articles
    bp.click_filter_by()
    bp.click_all_topics()
    top_articles = bp.top_articles
    return [cloud_and_dev_ops_articles, top_articles]


def test_is_there_more_than_1_cloud_dev_ops_article(articles_cache):
    assert len(articles_cache[0]) > 1


def test_is_there_more_than_1_top_article(articles_cache):
    assert len(articles_cache[1]) > 1


def test_are_articles_different(articles_cache):
    assert articles_cache[0] is not articles_cache[1]
