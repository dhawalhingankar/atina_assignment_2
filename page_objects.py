import time


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class BasePage:
    def __init__(self, driver):
        self.driver = driver

class WalletHubHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://wallethub.com/join/light"
        self.checkbox_locator = (By.XPATH, "//input[@name='embrace']")
        self.create_account_button_locator = (By.XPATH, "//button[@class='btn blue touch-element-cl']")

    def open(self):
        self.driver.get(self.url)

    def create_light_user_account(self, username, password):
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@id='em-ipt']").send_keys("dhingankar22@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@id='pw1-ipt']").send_keys("Sam@12mas")
        self.driver.find_element(By.XPATH, "//input[@id='pw2-ipt']").send_keys("Sam@12mas")
        checkbox = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.checkbox_locator))
        checkbox.click()
        create_account_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.create_account_button_locator))
        create_account_button.click()



class TestInsuranceCompanyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://wallethub.com/profile/test_insurance_company/"
        self.stars_locator = (By.CSS_SELECTOR, "review-star.rvs-svg.rvs-star")

    def open(self):
        self.driver.get(self.url)

    def hover_over_stars_and_click(self):
        stars = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(self.stars_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(stars[3]).perform()
        actions.move_to_element(stars[4]).click().perform()

    def select_policy(self, policy):
        policy_dropdown = self.driver.find_element_by_xpath("//review-star[@class='rvs-svg']//ancestor::div[@class='wh-rating-notes']//select")
        policy_dropdown.click()
        option = self.driver.find_element_by_xpath(f"//ul[@class='dropdown-list ng-star-inserted']//li[text()='{policy}']")
        option.click()


class ReviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.review_link_locator = (By.LINK_TEXT, "Write a review")
        self.review_textarea_locator = (By.ID, "review-content")
        self.submit_button_locator = (By.CSS_SELECTOR, "button[data-hook='user-review-submit']")

    def write_review(self, review_text):
        review_link = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(self.review_link_locator))
        review_link.click()
        review_textarea = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.review_textarea_locator))
        review_textarea.send_keys(review_text)

    def submit_review(self):
        submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.submit_button_locator))
        submit_button.click()

class ConfirmationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.confirmation_message_locator = (By.XPATH, "//div[@class='wh-section-cnt']//h4[text()='You have reviewed the institution.']")

    def is_confirmation_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.confirmation_message_locator))
            return True
        except:
            return False

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_reviews(self, username):
        reviews_url = f"https://wallethub.com/profile/{username}/reviews/"
        self.driver.get(reviews_url)

    def is_review_feed_displayed(self, review_text):
        review_feed_locator = (By.XPATH, f"//div[@class='rvtab-content']/div[contains(@class, 'rvtab-feed-review')]//p[text()='{review_text}']")
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(review_feed_locator))
            return True
        except:
            return False
