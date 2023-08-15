from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

from pollster.constants import PATH, BINARY_PATH
from pollster.constants import WEBSITE_URL as url


class Pollbot(webdriver.Firefox):
    def __init__(self, driver_path=PATH, teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown

        service = Service(PATH)
        option = webdriver.FirefoxOptions()
        option.binary_location = BINARY_PATH

        super(Pollbot, self).__init__(service=service, options=option)
        self.implicitly_wait(10)

    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()

    def main_page(self):
        self.get(url)

    def click_view_link(self):
        link = self.find_element(By.LINK_TEXT, "View Available Polls")
        link.click()

    def gender_vote(self, gender):
        def go_back():
            # Go back to polls page
            back_button = self.find_element(By.CLASS_NAME, "btn-secondary")
            back_button.click()

        def vote(gender):
            # Called when we get to polls page
            # Click on the gender user specifies
            if gender == "male":
                male_input = self.find_element(By.ID, "choice1")
                male_input.click()
            elif gender == "female":
                female_input = self.find_element(By.ID, "choice2")
                female_input.click()

            vote_button = self.find_element(By.CSS_SELECTOR, "input[value='Vote']")
            vote_button.click()
            go_back()

        card_bodys = self.find_elements(By.CLASS_NAME, "card-body")
        for card in card_bodys:
            if "gender" in str(card.get_attribute("innerHTML")).lower():
                vote_link = card.find_element(By.CLASS_NAME, "btn-primary")
                vote_link.click()  # This takes user to gender voting page

                vote(gender=gender.lower())

    def many_genders_vote(self, genders=[]):
        def vote_again():
            # Go back to polls page
            back_button = self.find_element(By.CLASS_NAME, "btn-secondary")
            back_button.click()

        def vote(gender):
            # Called when we get to polls page
            # Click on the gender user specifies
            if gender == "male":
                male_input = self.find_element(By.ID, "choice1")
                male_input.click()
            elif gender == "female":
                female_input = self.find_element(By.ID, "choice2")
                female_input.click()

            vote_button = self.find_element(By.CSS_SELECTOR, "input[value='Vote']")
            vote_button.click()

            vote_again()

        card_bodys = self.find_elements(By.CLASS_NAME, "card-body")
        for gender in genders:
            for card in card_bodys:
                if "gender" in str(card.get_attribute("innerHTML")).lower():
                    vote_link = card.find_element(By.CLASS_NAME, "btn-primary")
                    vote_link.click()  # This takes user to gender voting page

                    vote(gender=gender.lower())

    def adult_child_vote(self, vote_value):
        def go_back():
            back_button = self.find_element(By.CLASS_NAME, "btn-secondary")
            back_button.click()

        def vote(vote_value):
            if vote_value == "adult":
                adult_input = self.find_element(By.ID, "choice1")
                adult_input.click()
            elif vote_value == "child":
                child_input = self.find_element(By.ID, "choice2")
                child_input.click()

            vote_button = self.find_element(By.CSS_SELECTOR, "input[value='Vote']")
            vote_button.click()
            go_back()

        for card in card_bodys:
            card_bodys = self.find_elements(By.CLASS_NAME, "card-body")
            if "adult or child" in str(card.get_attribute("innerHTML")).lower():
                vote_link = card.find_element(By.LINK_TEXT, "Vote Now")
                vote_link.click()

                vote(vote_value=vote_value.lower())

    def many_adult_child_vote(self, vote_values=[]):
        def go_back():
            back_button = self.find_element(By.CLASS_NAME, "btn-secondary")
            back_button.click()

        def vote(vote_value):
            if vote_value == "adult":
                adult_input = self.find_element(By.ID, "choice1")
                adult_input.click()
            elif vote_value == "child":
                child_input = self.find_element(By.ID, "choice2")
                child_input.click()

            vote_button = self.find_element(By.CSS_SELECTOR, "input[value='Vote']")
            vote_button.click()
            go_back()

        for vote_value in vote_values:
            card_bodys = self.find_elements(By.CLASS_NAME, "card-body")
            for card in card_bodys:
                if "adult or child" in str(card.get_attribute("innerHTML")).lower():
                    vote_link = card.find_element(By.LINK_TEXT, "Vote Now")
                    vote_link.click()

                    vote(vote_value=vote_value.lower())
