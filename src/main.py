from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

WEBSITE_URL = "https://blog.griddynamics.com"


def main():
    pass


def get_in_touch(driver):
    """
    Case #3
    1. Open https://blog.griddynamics.com
    2. Click on Get In Touch button
    Ensure page Contact Us opened
    3. Fill in the following:
    First Name = Anna, Last Name = Smith
    email = annasmith@griddynamics.com
    4. instead of deprecated(select How did you hear about us? = Online Ads)
    Select what you interested in: careers / employment verification
    5. Click on checkbox “I have read and accepted the Terms & Conditions and
    Privacy Policy”
    6. Click on checkbox deprecated(“I allow Grid Dynamics to contact me”) - subscribe to newsletter
    7. Ensure Contact button is inactive
    :param driver: Selenium WebDriver instance.
    :return: string: submit button class
    """
    cookies_agree_button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(
            (By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
        )
    )

    cookies_agree_button.click()
    get_in_touch_xpath_locator = "//a[@href='https://www.griddynamics.com/contact']"
    get_in_touch_btn = driver.find_element(By.XPATH, get_in_touch_xpath_locator)
    get_in_touch_btn.click()
    WebDriverWait(driver, 5).until(
        ec.visibility_of_element_located((By.XPATH, "//div[@id='contact-page-form']"))
    )

    first_name = driver.find_element(
        By.XPATH, "//input[@id='get-in-touch-form-first_name']"
    )
    first_name.send_keys("Anna")

    last_name = driver.find_element(
        By.XPATH, "//input[@id='get-in-touch-form-last_name']"
    )
    last_name.send_keys("Smith")

    email = driver.find_element(By.XPATH, "//input[@id='get-in-touch-form-email']")
    email.send_keys("annasmith@griddynamics.com")

    interested_in = driver.find_element(
        By.XPATH, "//div[@class='get-in-touch-form__dropdown-current']"
    )
    interested_in.click()

    careers_employment = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, "//div[@key='careersemploymentverification']")
        )
    )
    careers_employment.click()

    terms_checkbox = driver.find_element(
        By.XPATH,
        "//input[@name='terms']/following-sibling::span[@class='wpcf7-list-item-label']",
    )

    if not terms_checkbox.is_selected():
        terms_checkbox.click()

    newsletter = driver.find_element(
        By.XPATH,
        "//input[@name='subscribe[]']/following-sibling::span[@class='wpcf7-list-item-label']",
    )

    if not newsletter.is_selected():
        newsletter.click()

    submit_btn_class = driver.find_element(
        By.XPATH, "//div[contains(@class, 'get-in-touch-form__field submit')]"
    ).get_attribute("class")
    return submit_btn_class


def find_articles(driver):
    """
    Case #2:
    1. Open https://blog.griddynamics.com
    2. Click ‘filter’ (check it’s visible and available)
    3. Filter by Cloud and DevOps topic
    4. Check there is more than 1 article
    5. Reset all filters
    6. Check the first article in the list is different than in step 4 and check there is more
    than 1 article.
    :param driver: Selenium WebDriver instance.
    :return: Dictionary with extracted data containing:
        - selected_category (str): CSS class of the selected category filter.
        - selected_filter_class (str): CSS class of the selected filter after clicking.
        - articles (list): List of filtered article elements.
        - selected_all_topics_class (str): CSS class of the "All Topics" filter after resetting.
        - top_articles (list): List of top articles displayed after resetting the filter.
    """
    filter_by_xpath_locator = "//div[@id='sub-category-list']"
    filter_by = driver.find_element(By.XPATH, filter_by_xpath_locator)
    filter_by.click()

    selected_category = filter_by.get_attribute("class")

    cloud_and_dev_ops_filter_locator = "//span[@data-id='13']"
    cloud_and_dev_ops_filter = driver.find_element(
        By.XPATH, cloud_and_dev_ops_filter_locator
    )
    cloud_and_dev_ops_filter.click()

    selected_filter_class = cloud_and_dev_ops_filter.get_attribute("class")

    articles = driver.find_elements(By.XPATH, "//div[@data-category-item='13']/*[2]/a")

    filter_by.click()
    all_topics_locator = "//span[@data-id='-2']"
    all_topics = driver.find_element(By.XPATH, all_topics_locator)
    all_topics.click()

    selected_all_topics_class = all_topics.get_attribute("class")

    top_articles = driver.find_elements(
        By.XPATH, "//div[@class='blog-page__feed']/*[1]/*[2]/a"
    )

    return {
        "selected_category": selected_category,
        "selected_filter_class": selected_filter_class,
        "articles": articles,
        "selected_all_topics_class": selected_all_topics_class,
        "top_articles": top_articles,
    }


def find_leonard_position(driver):
    """
    Case #1:
    1. Open https://blog.griddynamics.com
    2. Go to “Leadership” under About page
    3. Find Leonard Livschitz and click on the name
    4. Verify that information about Leonard has appeared.
    The text “Chief Executive Officer and Director” is visible.
      :return: Leonard Livschitz's position as a string.
    """
    leadership_under_about_xpath_locator = "//li[@id = 'menu-item-38744']//a[@href='https://www.griddynamics.com/leadership']"
    WebDriverWait(driver, 5).until(
        ec.presence_of_element_located((By.XPATH, leadership_under_about_xpath_locator))
    )
    leadership_under_about_link = driver.find_element(
        By.XPATH, leadership_under_about_xpath_locator
    )
    leadership_under_about_link.click()
    leonard_xpath_locator = (
        "//div [@class = 'team-grid__container team-grid__container--7']/*[1]"
    )
    leonard = driver.find_element(By.XPATH, leonard_xpath_locator)
    leonard.click()
    leonard_position_locator = "//div [@class = 'team-grid__container team-grid__container--7']/*[1]/div[@class ='team-grid__info']/*[2]/p"
    WebDriverWait(driver, 5).until(
        ec.visibility_of_element_located((By.XPATH, leonard_position_locator))
    )
    leonard_position = driver.find_element(By.XPATH, leonard_position_locator).text

    print(leonard_position)
    return leonard_position


if __name__ == "__main__":
    main()
