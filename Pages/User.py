from Pages.BasePages import BasePage
from selenium.webdriver.common.by import By
import pyautogui
import time
from selenium.webdriver.common.alert import Alert



class UserPage(BasePage):

    EnterUserName = (By.XPATH,"//form//input[@class='oxd-input oxd-input--active']")
    Search = (By.XPATH,"//button[contains(.,' Search ')]")
    usrname = (By.XPATH,"(//div[@class='oxd-table-cell oxd-padding-cell']/div)[2]")
    usrText = (By.XPATH,"(//div[@class='oxd-table-cell oxd-padding-cell']/div)[2]")
    edit_button = (By.XPATH,"//i[@class='oxd-icon bi-pencil-fill']")
    dropdown_button = (By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']/preceding::label[contains(.,'User Role')]")
    save_button = (By.XPATH,"//button[contains(.,' Save ')]")

    def __init__(self, driver):
        super().__init__(driver)

    def enterUsername_to_The_searchBox(self,data):
        self.Send_text(self.EnterUserName,data)

    def click_on_Search(self):
        self.Click_Element(self.Search)  

    def validate_user(self):
        username = self.navigate_element(self.usrText).text
        print ("Uersname === " ,username )
        assert username == "Admin"

    def click_on_Edit_button(self):
        self.Click_Element(self.edit_button)  

    def select_ess(self):
        self.Click_Element(self.dropdown_button)
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('enter')

    def click_save(self):
        self.Click_Element(self.save_button)

    def popupvalidation(self,validation):
        alert = Alert(self.driver) 
        alert_text = alert.text
        print("Alert Text:", alert_text)
        assert alert_text == validation
  


           





        
