import pytest
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities import excel_utils
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker

class Test_02_Admin_Login_data_driven:

    admin_page_url = Read_Config.get_admin_page_url()
    logger = Log_Maker.log_gen()
    path = "./test_data/admin_login_data.xlsx"
    status_list = []

    @pytest.mark.regression
    def test_valid_admin_login_data_driven(self,setup):
        self.logger.info("******************valid admin login check***********************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.driver.implicitly_wait(5)


        self.rows = excel_utils.get_row_count(self.path,"Sheet1")
        print("number of rows: ",self.rows)

        for r in range(2,self.rows+1):
            self.username = excel_utils.read_data(self.path,"Sheet1",r,1)
            self.password = excel_utils.read_data(self.path,"Sheet1",r,2)
            self.exp_login = excel_utils.read_data(self.path,"Sheet1",r,3)
            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            self.admin_lp.click_login()
            time.sleep(3)
            try:
                actual_dashboard_text = self.driver.find_element(By.XPATH, "//span[@class='title']").text
            except:
                actual_dashboard_text = "No data"
            expected_dashboard_text = "Products"
            if actual_dashboard_text == expected_dashboard_text:
                if self.exp_login == "Yes":
                    self.logger.info("test data is passed")
                    self.status_list.append("PASS")
                    self.admin_lp.click_logout()

                elif self.exp_login == "No":
                    self.logger.info("test data is failed")
                    self.status_list.append("FAIL")
                    self.admin_lp.click_logout()
            elif actual_dashboard_text != expected_dashboard_text:
                if self.exp_login == "Yes":
                    self.logger.info("test data is failed")
                    self.status_list.append("FAIL")
                elif self.exp_login == "No":
                    self.logger.info("test data is passed")
                    self.status_list.append("PASS")

        print("List status is : ",self.status_list)
        if "FAIL" in self.status_list:
            self.logger.info("Test Admin data is failed")
            assert False
        else:
            self.logger.info("Test Admin data is passed")
            assert True



