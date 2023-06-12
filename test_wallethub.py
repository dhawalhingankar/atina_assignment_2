import pytest
from selenium import webdriver
from Pages.page_objects import WalletHubHomePage, TestInsuranceCompanyPage, ReviewPage, ConfirmationPage, ProfilePage

@pytest.fixture(scope="module")
def driver():
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(executable_path="D:\\Driver\\chromedriver.exe")
    yield driver
    # Quit the browser after the test
    driver.quit()

@pytest.mark.usefixtures("driver")
def test_wallethub_actions(driver):
    # Set your credentials
    username = "dhingankar22@gmail.com"
    password = "Sam@12mas"

    # Create instances of the page classes
    home_page = WalletHubHomePage(driver)
    insurance_page = TestInsuranceCompanyPage(driver)
    review_page = ReviewPage(driver)
    confirmation_page = ConfirmationPage(driver)
    profile_page = ProfilePage(driver)

    # Step 1: Create a light user account
    home_page.open()
    home_page.create_light_user_account(username, password)

    # Step 2: Hover over the stars and click on the fourth and fifth star
    insurance_page.open()
    insurance_page.hover_over_stars_and_click()

    # Step 3: Change the value of the Policy dropdown to "Health"
    insurance_page.select_policy("Health")

    # Step 4: Write a review with random text
    review_text = "Project - Company Service World. We use our knowledge of local issues to identify areas of need, then apply our expertise and diverse perspectives to find a solution. Rotary members likely are working in your community right now to feed the hungry."
    review_page.write_review(review_text)

    # Step 5: Press submit
    review_page.submit_review()

    # Step 6: Verify the confirmation screen
    assert confirmation_page.is_confirmation_displayed(), "Confirmation screen not displayed"

    # Step 7: Verify the review feed in the profile page
    profile_page.open_reviews(username)
    assert profile_page.is_review_feed_displayed(review_text), "Review feed not found or does not match the entered review text"
