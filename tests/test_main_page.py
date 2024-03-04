from pages.main_page import MainPage


def test_main_page(browser):
    driver = browser

    driver.get('https://google.com')

    main_page = MainPage(driver)
    main_page.send_keys_search_textarea('Google')
    main_page.click_search_button()

    assert 'https://www.google.com/search' in main_page.get_current_url()
