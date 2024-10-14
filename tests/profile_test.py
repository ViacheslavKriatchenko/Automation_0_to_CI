import allure
import pytest
from base.base_test import BaseTest
import random


@allure.feature("Profile Functionality")
class TestProfile(BaseTest):

    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.Smoke
    def test_change_profile_name(self):

        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_info_button()
        self.personal_page.is_opened()
        self.personal_page.change_name(f'Test {random.randint(0, 10)}')
        self.personal_page.save_change()
        self.personal_page.is_changes_saved()
