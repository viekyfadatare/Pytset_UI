from selenium.webdriver.common.by import By
from Pages.BasePages import BasePage


class LoginPage(BasePage):
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


    username = (By.XPATH,"//input[@name='username']")
    password = (By.XPATH,"//input[@name='password']")
    login = (By.XPATH,"//button[contains(.,' Login ')]")

    def __init__(self, driver):
        super().__init__(driver)

    def open_application(self):
        self.driver.get(self.url)  

    def enter_username(self,usrname):
        self.Send_text(self.username,usrname)  

    def enter_password(self,passw):
        self.Send_text(self.password,passw)   

    def click_login_button(self):
        self.Click_Element(self.login)       




