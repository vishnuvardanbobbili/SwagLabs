import pytest
import time
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from base_pages.Place_Order import Place_Order
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker

class Test_03_place_order:

    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    firstname = Read_Config.get_firstname()
    lastname = Read_Config.get_lastname()
    postalcode = Read_Config.get_postalcode()
    logger = Log_Maker.log_gen()

    @pytest.mark.regression
    def test_place_order(self,setup):
        self.logger.info("******************valid admin login check***********************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        time.sleep(5)
        actual_dashboard_text = self.driver.find_element(By.XPATH, "//span[@class='title']").text
        if actual_dashboard_text == "Products":
            self.logger.info("******************Admin login is successful***********************")
            self.driver.save_screenshot("./screenshots/valid_admin_login.png")
        else:
            self.logger.info("******************Admin login is unsuccessful***********************")

        self.place_order = Place_Order(self.driver)
        self.place_order.click_backpack()
        self.place_order.click_tshirt()
        self.place_order.click_cart_link()
        self.place_order.click_checkout()
        self.place_order.enter_firstname(self.firstname)
        self.place_order.enter_lastname(self.lastname)
        self.place_order.enter_postalcode(self.postalcode)
        self.place_order.click_continue()
        time.sleep(5)
        self.place_order.click_finish()
        actual_order_message = self.driver.find_element(By.XPATH, "//h2[text() ='Thank you for your order!']").text
        expected_order_message = "Thank you for your order!"
        if actual_order_message == expected_order_message:
            self.logger.info("******************order placed successfully***********************")
            assert True
        else:
            self.logger.info("******************order not placed***********************")
            assert False
        self.place_order.click_back_home()
        self.driver.quit()



