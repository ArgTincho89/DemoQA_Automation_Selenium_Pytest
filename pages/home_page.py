
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    Elements = (By.CSS_SELECTOR, "#app > div > div > div.home-body > div > div:nth-child(1) > div > div.card-body > h5")
    Forms = (By.CSS_SELECTOR, "#app > div > div > div.home-body > div > div:nth-child(2) > div > div.card-body > h5")
    Alerts = (By.CSS_SELECTOR, "#app > div > div > div.home-body > div > div:nth-child(3) > div > div.card-body > h5")
    Widgets = (By.CSS_SELECTOR, "#app > div > div > div.home-body > div > div:nth-child(4) > div > div.card-body > h5")
    Interactions = (By.CSS_SELECTOR, "#app > div > div > div.home-body > div > div:nth-child(5) > div > div.card-body > h5")
    Book_store_application = (By.CSS_SELECTOR, "#app > div > div > div.home-body > div > div:nth-child(6) > div > div.card-body > h5")
    Text_Box_button = (By.CSS_SELECTOR, "div.element-group:nth-of-type(1) #item-0")
    def __init__(self, driver):
        super().__init__(driver)
        
    