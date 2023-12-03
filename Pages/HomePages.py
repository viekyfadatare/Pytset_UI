from selenium.webdriver.common.by import By
from Pages.BasePages import BasePage


class HomePage(BasePage):

    Admin = (By.XPATH,"//ul[@class='oxd-main-menu']/li[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def validate_homePage(self):
        Title = self.driver.title
        assert Title == "OrangeHRM", "Homepage Validation Done Successfully"

    def Click_on_Admin(self):
        self.Click_Element(self.Admin)    
