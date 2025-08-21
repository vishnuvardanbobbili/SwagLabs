from selenium.webdriver.common.by import By


class Place_Order:

    button_backpack_id = "add-to-cart-sauce-labs-backpack"
    button_tshirt_id = "add-to-cart-sauce-labs-bolt-t-shirt"
    link_cart_xpath = "//a[@data-test = 'shopping-cart-link']"
    button_checkout_id = "checkout"
    textbox_first_name_id = "first-name"
    textbox_last_name_id = "last-name"
    textbox_postal_code_id = "postal-code"
    button_continue_id = "continue"
    button_finish_id = "finish"
    button_back_home_id = "back-to-products"

    def __init__(self, driver):
        self.driver = driver

    def click_backpack(self):
        self.driver.find_element(By.ID, self.button_backpack_id).click()

    def click_tshirt(self):
        self.driver.find_element(By.ID, self.button_tshirt_id).click()

    def click_cart_link(self):
        self.driver.find_element(By.XPATH, self.link_cart_xpath).click()

    def click_checkout(self):
        self.driver.find_element(By.ID, self.button_checkout_id).click()

    def enter_firstname(self, firstname):
        self.driver.find_element(By.ID, self.textbox_first_name_id).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.ID, self.textbox_last_name_id).send_keys(lastname)

    def enter_postalcode(self, postalcode):
        self.driver.find_element(By.ID, self.textbox_postal_code_id).send_keys(postalcode)

    def click_continue(self):
        self.driver.find_element(By.ID, self.button_continue_id).click()

    def click_finish(self):
        self.driver.find_element(By.ID, self.button_finish_id).click()

    def click_back_home(self):
        self.driver.find_element(By.ID, self.button_back_home_id).click()


