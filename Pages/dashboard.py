
from selenium.webdriver.common.by import By
from Pages.BasePages import BasePage

class DashboardPage(BasePage):


    LBL_DashBoard = (By.XPATH,"//span[@class='oxd-topbar-header-breadcrumb']//h6[1]")
    text = ""
    LNK_Navigation_Menu = (By.XPATH,"//span[text()={}]".format(text))
    BTN_Account_Action = (By.XPATH,"//i[contains(@class,'oxd-icon bi-caret-down-fill')]")
    LNK_Logout =(By.LINK_TEXT,"Logout")
    TXTBOX_Search_user = (By.XPATH,"//label[text()='Username']/following::input")
    BTN_Search_user =(By.XPATH,"//button[text()=' Reset ']//following-sibling::button")

    def __init__(self, driver):
        super().__init__(driver)

    def Click_Logout_link(self):
        self.Click_Element(self.BTN_Account_Action) 
        self.Click_Element(self.LNK_Logout)   
    
    def goto_navigation_menu(self,name):
        text = name
        self.Click_Element(self.LNK_Navigation_Menu)

    def enter_text_to_search_user(self,user_name):
        self.Send_text(self.TXTBOX_Search_user,user_name)   


    def click_search_user(self):
        self.Click_Element(self.BTN_Search_user)     