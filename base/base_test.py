import pytest
from pages.login_page import LoginPage
from pages.dashbord_page import DashbordPage
from pages.personal_page import PersonalPage
from config.data import Data


class BaseTest:

    data: Data

    login_page: LoginPage
    dashboard_page: DashbordPage
    personal_page: PersonalPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.data = Data()
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashbordPage(driver)
        request.cls.personal_page = PersonalPage(driver)
