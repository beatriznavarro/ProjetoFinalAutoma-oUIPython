from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.PageObject import PageObject


class MenuPage(PageObject):

    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    btn_bank_manager = 'button.btn.btn-primary.btn-lg[ng-click="manager()"]'
    btn_customer_login = 'button.btn.btn-primary.btn-lg[ng-click="customer()"]'

    def __init__(self, browser):
        super(MenuPage, self).__init__(browser=browser)
        self.driver.get(self.url)

    def open_customer_login(self):
        btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.btn_customer_login)))
        btn.click()

    def open_bank_manager_login(self):
        btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.btn_bank_manager)))
        btn.click()
