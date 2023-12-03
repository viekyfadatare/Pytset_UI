from selenium.webdriver.common.by import By
from Pages.BasePages import BasePage

class LogoutPage(BasePage):

    profileicon = (By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
    Logout = (By.XPATH,"//a[contains(.,'Logout')]")

    

    def __init__(self, driver):
        super().__init__(driver)

    def clickonProgfileIcone(self):
        self.Click_Element(self.profileicon)

    def clickon_Logout(self):
        self.Click_Element(self.Logout)    
        




  