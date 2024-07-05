from datetime import datetime, timedelta

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import base_page
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class InteractionsPage(BasePage):
    
    # Sortable elements locators.
    interactions_sortable_section_button = (By.CSS_SELECTOR, "div.left-pannel div.element-group:nth-of-type(5) div.element-list ul #item-0")
    interactions_sortable_section_title = (By.CSS_SELECTOR, "h1.text-center")
    interactions_sortable_list_button = (By.ID, "demo-tab-list")
    interactions_sortable_grid_button = (By.ID, "demo-tab-grid")
    interactions_sortable_list_one_button = (By.XPATH, "//div[@id='demo-tabpane-list']//div[contains(text(), 'One')]")
    
    def get_current_order(self, xpath):
        # Function to get the current order of the items.
        elements = self.driver.find_elements(By.XPATH, xpath)  
        return [element.text for element in elements]
        
    def drag_and_drop_below(self, base_xpath, source_text, target_text):
         # Function to drag an object and drop it where we want
        source =  self.driver.find_element(By.XPATH, f"{base_xpath}//div[contains(text(), '{source_text}')]")
        target = self.driver.find_element(By.XPATH, f"{base_xpath}//div[contains(text(), '{target_text}')]") 
        ActionChains(self.driver).drag_and_drop(source, target).perform()
        
    # Selectable elements locators.
    interactions_selectable_section_button = (By.CSS_SELECTOR, "div.left-pannel div.element-group:nth-of-type(5) div.element-list ul #item-1")
    interactions_selectable_section_title = (By.CSS_SELECTOR, "h1.text-center")
    interactions_selectable_list_button = (By.ID, "demo-tab-list")
    interactions_selectable_grid_button = (By.ID, "demo-tab-grid")

    # Resizable elements locators.
    interactions_resizable_section_button = (By.CSS_SELECTOR, "div.left-pannel div.element-group:nth-of-type(5) div.element-list ul #item-2")
    interactions_resizable_section_title = (By.CSS_SELECTOR, "h1.text-center")
    
    # Droppable elements locators.
    interactions_droppable_section_button = (By.CSS_SELECTOR, "div.left-pannel div.element-group:nth-of-type(5) div.element-list ul #item-3")
    interactions_droppable_section_title = (By.CSS_SELECTOR, "h1.text-center")
    interactions_droppable_simple_drag_box = (By.ID, "draggable")
    interactions_droppable_simple_drop_box = (By.ID, "droppable")
    interactions_droppable_accept_tab_button = (By.ID, "droppableExample-tab-accept")
    interactions_droppable_accept_not_acceptable_drag = (By.ID, "notAcceptable")
    interactions_droppable_accept_acceptable_drag = (By.ID, "acceptable")
    interactions_droppable_accept_drop_box = (By.CSS_SELECTOR, "div#droppableExample-tabpane-accept #droppable")
    interactions_droppable_prevent_propagation_tab_button = (By.ID, "droppableExample-tab-preventPropogation")
    interactions_droppable_prevent_propagation_drag = (By.ID, "dragBox")
    interactions_droppable_prevent_propagation_not_greedy_inner_drop_box = (By.ID, "notGreedyInnerDropBox")
    interactions_droppable_prevent_propagation_not_greedy_outer_drop_box = (By.ID, "notGreedyDropBox")
    interactions_droppable_prevent_propagation_greedy_inner_drop_box = (By.ID, "greedyDropBoxInner")
    interactions_droppable_prevent_propagation_greedy_outer_drop_box = (By.ID, "greedyDropBox")
    interactions_droppable_revert_tab_button = (By.ID, "droppableExample-tab-revertable")
    interactions_droppable_revert_will_revert = (By.ID, "revertable")
    interactions_droppable_revert_not_revert = (By.ID, "notRevertable")
    interactions_droppable_revert_drop_box = (By.CSS_SELECTOR, "div#droppableExample-tabpane-revertable #droppable")
    
    
    def drag_and_drop_with_highlight_check(self, drag_selector, drop_selector, highlight=True):
        # Find the elements to drag and drop
        drag_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(drag_selector)
        )
        drop_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(drop_selector)
        )
        # Performs the action of dragging and dropping
        ActionChains(self.driver).click_and_hold(drag_element).move_to_element(drop_element).release().perform()  
        # Checks the correct result
        class_attribute = drop_element.get_attribute("class")
        if highlight:
            assert "highlight" in class_attribute, "Drop box does not have 'highlight' class."
        else:
            assert "highlight" not in class_attribute, "Drop box should not have 'highlight' class."
            
            
    # Dragabble elements locators.
    interactions_dragabble_section_button = (By.CSS_SELECTOR, "div.left-pannel div.element-group:nth-of-type(5) div.element-list ul #item-4")
    interactions_dragabble_section_title = (By.CSS_SELECTOR, "h1.text-center")
    interactions_dragabble_simple_drag = (By.CSS_SELECTOR, "div#draggableExample-tabpane-simple #dragBox")
    interactions_dragabble_axis_restricted_tab_button = (By.ID, "draggableExample-tab-axisRestriction")
    interactions_dragabble_axis_restricted_x_drag = (By.CSS_SELECTOR, "div#draggableExample-tabpane-axisRestriction #restrictedX")
    interactions_dragabble_axis_restricted_y_drag = (By.CSS_SELECTOR, "div#draggableExample-tabpane-axisRestriction #restrictedY")
    interactions_dragabble_container_restricted_tab_button = (By.ID, "draggableExample-tab-containerRestriction")
    interactions_dragabble_container_restricted_box_contained = (By.CSS_SELECTOR, "#containmentWrapper div")
    interactions_dragabble_container_restricted_container = (By.ID, "containmentWrapper")
    interactions_dragabble_container_restricted_parent_container = (By.CSS_SELECTOR, "#draggableExample-tabpane-containerRestriction div:nth-of-type(2)")
    interactions_dragabble_container_restricted_parent_drag = (By.CSS_SELECTOR, "#draggableExample-tabpane-containerRestriction div:nth-of-type(2) span")
        

    def drag_element(self, drag_selector, move_x, move_y):
        # Find the element to move
        drag_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(drag_selector)
        )
        # Performs the movement of the element
        action = ActionChains(self.driver)
        action.click_and_hold(drag_element).move_by_offset(move_x, move_y).release().perform()
        
     