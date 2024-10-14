import time
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class PersonalPage(BasePage):

    PAGE_URL = Links.PERSONAL_PAGE

    FIRSTNAME_FIELD = ("xpath", "//input[@name='firstName']")
    SAVE_BUTTON = ("xpath", "//button[@type='submit'][1]")

    def change_name(self, new_name):
        with allure.step(f"Change name on {new_name}"):
            input_firstname_field = self.wait.until(
                EC.element_to_be_clickable((self.FIRSTNAME_FIELD))
                )
            input_firstname_field.send_keys(Keys.LEFT_CONTROL + "A")
            input_firstname_field.send_keys(Keys.BACKSPACE)
            assert input_firstname_field.get_attribute('value') == "", 'Очисти поле'
            input_firstname_field.send_keys(new_name)
            self.name = new_name

    @allure.step("Save changes")
    def save_change(self):
        self.wait.until(
            EC.element_to_be_clickable((self.SAVE_BUTTON))
            ).click()

    @allure.step("Changes has been changed succsfuly")
    def is_changes_saved(self):
        self.wait.until(
            EC.text_to_be_present_in_element_value(
                self.FIRSTNAME_FIELD, self.name
                )
            )
