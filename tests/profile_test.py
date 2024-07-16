from base.base_test import BaseTest


class TestProfile(BaseTest):

    def test_change_profile_name(self):

        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_login(login)
        self.login_page.enter_password(password)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_info_button()
        self.personal_page.is_opened()
        self.personal_page.change_name()
        self.personal_page.save_change()
