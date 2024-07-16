from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class PersonalPage(BasePage):

    PAGE_URL = Links.PERSONAL_PAGE

    FIRSTNAME_FIELD = ("xpath", "//input[@name='firstName']")
    SAVE_BUTTON = ("xpath", "//button[@type='submit'][1]")

    def change_name(self, new_name):

        input_firstname_field = self.wait.until(
            EC.element_to_be_clickable((self.FIRSTNAME_FIELD))
            )
        input_firstname_field.clear()
        assert input_firstname_field.get_attribute('value') == "", 'Текст не удален'
        input_firstname_field.send_keys(self.new_name)

    def save_change(self):

        self.wait.until(
            EC.element_to_be_clickable((self.SAVE_BUTTON_BUTTON))
            ).click()
