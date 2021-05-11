from selenium.webdriver.common.by import By
import sys
sys.path.append("tests/acceptance/locators")
sys.path.append("tests/acceptance/page_model")
from locators.new_post_page import NewPostLocators
from page_model.base_page import BasePage


class NewPostPage(BasePage):
    @property
    def url(self):
        return super(NewPostPage, self).url + '/post'
    
    
    @property
    def form(self):
        return self.driver.find_element(*NewPostLocators.NEW_POST_FORM)
    
    
    @property
    def submit_button(self):
        return self.driver.find_element(*NewPostLocators.SUBMIT_BUTTON)
    
    def form_field(self, name):
        return self.form.find_element(By.NAME, name)
    
