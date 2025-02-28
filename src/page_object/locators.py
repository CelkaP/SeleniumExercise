class Locator(object):
    # Blog Page
    cookies_agree_button = "//button[@id='onetrust-accept-btn-handler']"

    leadership_under_about = "//li[@id = 'menu-item-38744']//a[@href='https://www.griddynamics.com/leadership']"

    filter_by = "//div[@id='sub-category-list']"

    cloud_and_dev_ops_filter = "//span[@data-id='13']"

    articles = "//div[@data-category-item='13']/*[2]/a"

    top_articles = "//div[@class='blog-page__feed']/*[1]/*[2]/a"

    all_topics = "//span[@data-id='-2']"

    get_in_touch_button = "//a[@href='https://www.griddynamics.com/contact']"

    # Leadership Page
    leonard = "//div[@class='team-grid__container team-grid__container--7']/*[1]"

    # Leader Page
    leonard_position = "//div[@class='team-grid__modal-content-description']/div[@class='team-grid__modal-content-bio--position']/p[1]"
    # "//div [@class = 'team-grid__container team-grid__container--7']/*[2]/div[@class='team-grid__modal-content']/div[@class='team-grid__modal-content-description']/div[@class='team-grid__modal-content-bio--position']/p"

    leonard_bio = "//div [@class = 'team-grid__container team-grid__container--7']/*[2]/div[@class='team-grid__modal-content']/div[@class='team-grid__modal-content-bio']/p/*[1]"

    # Get In Touch Page
    first_name = "//input[@id='get-in-touch-form-first_name']"

    last_name = "//input[@id='get-in-touch-form-last_name']"

    email = "//input[@id='get-in-touch-form-email']"

    interested_in = "//div[@class='get-in-touch-form__dropdown-current']"

    careers_employment = "//div[@key='careersemploymentverification']"

    terms_checkbox = (
        "//input[@name='terms']/following-sibling::span[@class='wpcf7-list-item-label']"
    )

    newsletter = "//input[@name='subscribe[]']/following-sibling::span[@class='wpcf7-list-item-label']"

    submit_btn = "//div[contains(@class, 'get-in-touch-form__field submit')]"
