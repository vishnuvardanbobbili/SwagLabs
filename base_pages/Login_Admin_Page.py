import time

from selenium.webdriver.common.by import By


class Login_Admin_Page:

    textbox_username_id = "user-name"
    textbox_password_id = "password"
    button_login_id = "login-button"
    button_all_items_id = "react-burger-menu-btn"
    button_logout_xpath = "//a[@id = 'logout_sidebar_link']"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID,self.button_login_id).click()

    def click_logout(self):
        self.driver.find_element(By.ID,self.button_all_items_id).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()
