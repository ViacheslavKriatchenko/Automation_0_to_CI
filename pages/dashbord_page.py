from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class DashbordPage(BasePage):

    PAGE_URL = Links.DASHBORD_PAGE

    info_button = ("xpath", "//span[text()='My Info']")

    def click_info_button(self):

        self.wait.until(
            EC.element_to_be_clickable((self.info_button))
            ).click()
