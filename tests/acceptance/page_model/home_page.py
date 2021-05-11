import sys
sys.path.append("tests/acceptance/page_model")
sys.path.append("tests/acceptance/locators")
from locators.home_page import HomePageLocators
from page_model.base_page import BasePage

class HomePage(BasePage):
    @property    
    def url(self):
        return super(HomePage, self).url + '/'
    

    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.NAVIGATION_LINK)
    
    
