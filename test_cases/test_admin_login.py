import pytest
import time
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker

class Test_01_Admin_Login:

    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger = Log_Maker.log_gen()

    @pytest.mark.sanity
    def test_title_verification(self, setup):
        self.logger.info("******************Test_01_Admin_Login***********************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        expected_name = "Swag Labs"
        actual_title = self.driver.title
        if actual_title == expected_name:
            self.logger.info("********************Title verification is successful*********************")
            self.driver.save_screenshot("./screenshots/page_title.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("********************Title verification is unsuccessful*********************")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_valid_admin_login(self,setup):
        self.logger.info("******************valid admin login check***********************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        actual_dashboard_text = self.driver.find_element(By.XPATH, "//span[@class='title']").text
        if actual_dashboard_text == "Products":
            self.logger.info("******************Admin login is successful***********************")
            assert True
            self.driver.save_screenshot("./screenshots/valid_admin_login.png")
            self.driver.close()
        else:
            self.logger.info("******************Admin login is unsuccessful***********************")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_invalid_admin_login(self, setup):
        self.logger.info("******************Invalid admin login check***********************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        actual_dashboard_text = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        if actual_dashboard_text == "Epic sadface: Username and password do not match any user in this service":
            self.logger.info("******************Invalid login successful***********************")
            assert True
            self.driver.save_screenshot("./screenshots/invalid_admin_login.png")
            self.driver.quit()
        else:
            self.logger.info("******************Invalid login unsuccessful***********************")
            self.driver.quit()
            assert False
