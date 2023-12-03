from argparse import Action
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.action_chains import ActionChains




class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def Click_Element(self,locator):
        WebDriverWait(self.driver,10).until(Ec.element_to_be_clickable(locator)).click()

    def Send_text(self,locator,text):
        WebDriverWait(self.driver,10).until(Ec.visibility_of_element_located(locator)).send_keys(text)

    def Select_By_Visible_Text(self,locator,text):
        Select(WebDriverWait(self.driver,10).until(Ec.visibility_of_element_located(locator))).select_by_visible_text

    def Get_Element_Text(self,locator,text):
        return WebDriverWait(self.driver,10).until(Ec.visibility_of_element_located(locator)).text

    def mouse_over(self ,locator):
        element = WebDriverWait(self.driver,10).until(Ec.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform

    def element_displayed(self,locator):
        return  WebDriverWait(self.driver,10).until(Ec.visibility_of_element_located(locator)).is_displayed   
    
    def navigate_element(self,locator):
        return  WebDriverWait(self.driver,10).until(Ec.visibility_of_element_located(locator))


        
