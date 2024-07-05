import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from pages.home_page import HomePage
from pages.interactions_page import InteractionsPage
from tests.base_test import BaseTest




class TestInteractions(BaseTest):
    
    def test_01_sortable_list(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Interactions
        interactions_link = home_page.find(*home_page.Interactions)
        self.driver.execute_script("arguments[0].click();", interactions_link)
        # Creation of an Interactions Page instance
        interactions_page = InteractionsPage(self.driver)
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        # Navigate to Droppable section
        interactions_page.click(*interactions_page.interactions_sortable_section_button)
        # Asserting that the tittle of the section corresponds to Sortable
        interactions_page.assert_text(interactions_page.interactions_sortable_section_title, "Sortable")
        # scrolls down 10% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.1);")
        time.sleep(1)
        # Grabs the "One" element, moves it 1 step bellow each time and checks that the position is correct.
        elements_text = ["Two", "Three", "Four", "Five", "Six"]
        base_xpath = "//div[@id='demo-tabpane-list']"
        order_xpath = "//div[@id='demo-tabpane-list']//div[contains(@class, 'vertical-list-container mt-4')]//div"
        for i, text in enumerate(elements_text, start=1):  
            interactions_page.drag_and_drop_below(base_xpath,"One", text)
            time.sleep(0.5)
            current_order = interactions_page.get_current_order(order_xpath)
            if i < len(elements_text):
                next_element_index = current_order.index(elements_text[i])
                assert current_order[next_element_index - 1] == "One", f"'One' is not in the correct position after moving it bellow '{text}'"
            else:
                assert current_order[0] != "One" 


    def test_02_sortable_grid(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Interactions
        interactions_link = home_page.find(*home_page.Interactions)
        self.driver.execute_script("arguments[0].click();", interactions_link)
        # Creation of an Interactions Page instance
        interactions_page = InteractionsPage(self.driver)
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        time.sleep(0.5)
        # Navigate to Droppable section
        interactions_page.click(*interactions_page.interactions_sortable_section_button)
        # Asserting that the tittle of the section corresponds to Sortable
        interactions_page.assert_text(interactions_page.interactions_sortable_section_title, "Sortable")
        # Clicks the "Grid" button
        interactions_page.click(*interactions_page.interactions_sortable_grid_button)
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        time.sleep(0.5)
        # Grabs the "One" element, moves it 1 step bellow each time and checks that the position is correct.
        elements_text = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        base_xpath = "//div[@id='demo-tabpane-grid']"
        order_xpath = "//*[@id='demo-tabpane-grid']//div[contains(@class, 'grid-container mt-4')]//div"
        for i, text in enumerate(elements_text, start=1):  
            interactions_page.drag_and_drop_below(base_xpath,"One", text)
            time.sleep(0.5)
            current_order = interactions_page.get_current_order(order_xpath)
            if i < len(elements_text):
                next_element_index = current_order.index(elements_text[i])
                assert current_order[next_element_index - 1] == "One", f"'One' is not in the correct position after moving it bellow '{text}'"
            else:
                assert current_order[0] != "One" 
                
    def test_03_selectable_list(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Interactions
        interactions_link = home_page.find(*home_page.Interactions)
        self.driver.execute_script("arguments[0].click();", interactions_link)
        # Creation of an Interactions Page instance
        interactions_page = InteractionsPage(self.driver)
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        time.sleep(0.5)
        # Navigate to Droppable section
        interactions_page.click(*interactions_page.interactions_selectable_section_button)
        # Asserting that the tittle of the section corresponds to Sortable
        interactions_page.assert_text(interactions_page.interactions_selectable_section_title, "Selectable")
        # scrolls down 10% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.1);")
        time.sleep(0.5)
        # Selects all four elements and checks that they become "active"
        for i in range(1, 5):
            selector = "ul#verticalListContainer li:nth-of-type({})".format(i)
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
            )
            element.click()
            class_attribute = element.get_attribute('class')
            assert 'active' in class_attribute, f"Element {i} is not active." 
            
    def test_04_selectable_grid(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Interactions
        interactions_link = home_page.find(*home_page.Interactions)
        self.driver.execute_script("arguments[0].click();", interactions_link)
        # Creation of an Interactions Page instance
        interactions_page = InteractionsPage(self.driver)
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        time.sleep(0.5)
        # Navigate to Droppable section
        interactions_page.click(*interactions_page.interactions_selectable_section_button)
        # Asserting that the tittle of the section corresponds to Sortable
        interactions_page.assert_text(interactions_page.interactions_selectable_section_title, "Selectable")
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        time.sleep(1)
        # Accesing the grid section.
        interactions_page.click(*interactions_page.interactions_selectable_grid_button)
        # Selects all nine items and checks that they become "active"
        for row in range(1, 4):
            for item in range(1, 4):
                selector = f"div#gridContainer div#row{row} li:nth-of-type({item})"
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                )
                element.click()
                class_attribute = element.get_attribute('class')
                assert 'active' in class_attribute, f"Element in row {row}, item {item} is not active." 
        
    def test_05_resizable(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Interactions
        interactions_link = home_page.find(*home_page.Interactions)
        self.driver.execute_script("arguments[0].click();", interactions_link)
        # Creation of an Interactions Page instance
        interactions_page = InteractionsPage(self.driver)
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        time.sleep(0.5)
        # Navigate to Droppable section
        interactions_page.click(*interactions_page.interactions_resizable_section_button)
        # Asserting that the tittle of the section corresponds to Sortable
        interactions_page.assert_text(interactions_page.interactions_resizable_section_title, "Resizable")
        # scrolls down 10% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.1);")
        time.sleep(1)
        # Accesses the resizable element and changes it's size asserting the correct changes
        resizable_handle = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#resizableBoxWithRestriction span"))
        )
        # Checks initial size of 200x200
        resizable_box = self.driver.find_element(By.ID, "resizableBoxWithRestriction")
        initial_style = resizable_box.get_attribute("style")
        assert "width: 200px; height: 200px;" in initial_style, "Initial size is not 200x200."
        # Changes size to 150x150 and asserts correct size
        ActionChains(self.driver).click_and_hold(resizable_handle).move_by_offset(-50, -50).release().perform()
        WebDriverWait(self.driver, 10).until(
            lambda driver: "width: 150px; height: 150px;" in resizable_box.get_attribute("style")
        )
        assert "width: 150px; height: 150px;" in resizable_box.get_attribute("style"), "Size is not 150x150 after resize."
        # Changes size to 500x300 and asserts correct size
        ActionChains(self.driver).click_and_hold(resizable_handle).move_by_offset(350, 150).release().perform()
        WebDriverWait(self.driver, 10).until(
            lambda driver: "width: 500px; height: 300px;" in resizable_box.get_attribute("style")
        )
        assert "width: 500px; height: 300px;" in resizable_box.get_attribute("style"), "Size is not 500x300 after resize." 
        
    def test_06_droppable_simple(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Interactions
        interactions_link = home_page.find(*home_page.Interactions)
        self.driver.execute_script("arguments[0].click();", interactions_link)
        # Creation of an Interactions Page instance
        interactions_page = InteractionsPage(self.driver)
        # scrolls down 30% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.3);")
        time.sleep(0.5)
        # Navigate to Droppable section
        interactions_page.click(*interactions_page.interactions_droppable_section_button)
        # Asserting that the tittle of the section corresponds to Sortable
        interactions_page.assert_text(interactions_page.interactions_droppable_section_title, "Droppable")
        # scrolls down 10% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.1);")
        time.sleep(1)
        # Drags the "Drag me" element and drops it in the "Drop here"
        interactions_page.drag_and_drop_with_highlight_check(interactions_page.interactions_droppable_simple_drag_box,
                                                             interactions_page.interactions_droppable_simple_drop_box) 
        
    def test_07_droppable_simple(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Interactions
        interactions_link = home_page.find(*home_page.Interactions)
        self.driver.execute_script("arguments[0].click();", interactions_link)
        # Creation of an Interactions Page instance
        interactions_page = InteractionsPage(self.driver)
        # scrolls down 30% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.3);")
        time.sleep(0.5)
        # Navigate to Droppable section
        interactions_page.click(*interactions_page.interactions_droppable_section_button)
        # Asserting that the tittle of the section corresponds to Sortable
        interactions_page.assert_text(interactions_page.interactions_droppable_section_title, "Droppable")
        # scrolls down 10% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.1);")
        time.sleep(1)
        # Click the "Accept" tab
        interactions_page.click(*interactions_page.interactions_droppable_accept_tab_button)
        # Performs the drag and drop action of the "not acceptable" drag box and checks the drop box is not highlighted
        interactions_page.drag_and_drop_with_highlight_check(
            interactions_page.interactions_droppable_accept_not_acceptable_drag,
            interactions_page.interactions_droppable_accept_drop_box,
            highlight=False
        )
        # Performs the drag and drop action of the "acceptable" drag box and checks the drop box is not highlighted
        interactions_page.drag_and_drop_with_highlight_check(
            interactions_page.interactions_droppable_accept_acceptable_drag,
            interactions_page.interactions_droppable_accept_drop_box,
            highlight=True
        )
        
    def test_08_droppable_prevent_propagation(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Interactions
        interactions_link = home_page.find(*home_page.Interactions)
        self.driver.execute_script("arguments[0].click();", interactions_link)
        # Creation of an Interactions Page instance
        interactions_page = InteractionsPage(self.driver)
        # scrolls down 30% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.3);")
        time.sleep(0.5)
        # Navigate to Droppable section
        interactions_page.click(*interactions_page.interactions_droppable_section_button)
        # Asserting that the tittle of the section corresponds to Sortable
        interactions_page.assert_text(interactions_page.interactions_droppable_section_title, "Droppable")
        # scrolls down 10% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.1);")
        time.sleep(1)
        # Click the "Prevent propagation" tab
        interactions_page.click(*interactions_page.interactions_droppable_prevent_propagation_tab_button)
        # Dragging the "Drag Me" element to the "Not greedy" Inner drop box and checking that both the inner and outer boxes are highlighted
        interactions_page.drag_and_drop_with_highlight_check(
            interactions_page.interactions_droppable_prevent_propagation_drag,
            interactions_page.interactions_droppable_prevent_propagation_not_greedy_inner_drop_box,
            highlight=True
        )
        outer_droppable = interactions_page.find(*interactions_page.interactions_droppable_prevent_propagation_not_greedy_outer_drop_box)
        class_attribute = outer_droppable.get_attribute("class")
        assert "highlight" in class_attribute, "Drop box does not have 'highlight' class."
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        time.sleep(1)
        # Dragging the "Drag Me" element to the "Greedty" inner drop box and checking that it gets highlighed but the outer drop box doesn't get highlighted
        interactions_page.drag_and_drop_with_highlight_check(
            interactions_page.interactions_droppable_prevent_propagation_drag,
            interactions_page.interactions_droppable_prevent_propagation_greedy_inner_drop_box,
            highlight=True
        )
        outer_droppable = interactions_page.find(*interactions_page.interactions_droppable_prevent_propagation_greedy_outer_drop_box)
        class_attribute = outer_droppable.get_attribute("class")
        assert "highlight" not in class_attribute, "Drop box has 'highlight' class." ""
        
    def test_09_droppable_revert_dragabble(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Interactions
        interactions_link = home_page.find(*home_page.Interactions)
        self.driver.execute_script("arguments[0].click();", interactions_link)
        # Creation of an Interactions Page instance
        interactions_page = InteractionsPage(self.driver)
        # scrolls down 30% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.3);")
        time.sleep(0.5)
        # Navigate to Droppable section
        interactions_page.click(*interactions_page.interactions_droppable_section_button)
        # Asserting that the tittle of the section corresponds to Sortable
        interactions_page.assert_text(interactions_page.interactions_droppable_section_title, "Droppable")
        # scrolls down 10% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.1);")
        time.sleep(1)
        # Click the "Prevent propagation" tab
        interactions_page.click(*interactions_page.interactions_droppable_revert_tab_button)
        # scrolls down 10% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.1);")
        # Moving the "Will revert" element to the dropbox and checking it has not changed location
        interactions_page.drag_and_drop_with_highlight_check(
            interactions_page.interactions_droppable_revert_will_revert,
            interactions_page.interactions_droppable_revert_drop_box)
        time.sleep(1)
        element = interactions_page.find(*interactions_page.interactions_droppable_revert_will_revert)
        element_style = element.get_attribute("style")
        assert "left: 0px" in element_style and "top: 0px" in element_style, "left or top are not 0"
        # Moving the "not revert" element to the dropbox and checking it has changed location
        interactions_page.drag_and_drop_with_highlight_check(
            interactions_page.interactions_droppable_revert_not_revert,
            interactions_page.interactions_droppable_revert_drop_box)
        element = interactions_page.find(*interactions_page.interactions_droppable_revert_not_revert)
        element_style = element.get_attribute("style")
        assert "left: 0px" not in element_style and "top: 0px" not in element_style, "left or top are 0" 
        
    def test_10_dragabble_simple(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Interactions
        interactions_link = home_page.find(*home_page.Interactions)
        self.driver.execute_script("arguments[0].click();", interactions_link)
        # Creation of an Interactions Page instance
        interactions_page = InteractionsPage(self.driver)
        # scrolls down 30% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.3);")
        time.sleep(0.5)
        # Navigate to dragabble section
        interactions_page.click(*interactions_page.interactions_dragabble_section_button)
        # Asserting that the tittle of the section corresponds to Sortable
        interactions_page.assert_text(interactions_page.interactions_dragabble_section_title, "Dragabble")
        # Scrolls to the section title to enable better elements visibility
        section_title = interactions_page.find(*interactions_page.interactions_dragabble_section_title)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", section_title)
        # Moving the "Drag me" element to the side and down and asserting the correct positions
        interactions_page.drag_element(interactions_page.interactions_dragabble_simple_drag,
                                          220, 60)
        # Asserting the correct position of the element
        element = interactions_page.find(*interactions_page.interactions_dragabble_simple_drag)
        element_style = element.get_attribute("style")
        assert "left: 220px" and "top: 60px" in element_style  
      
    def test_11_dragabble_axis_restricted(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Interactions
        interactions_link = home_page.find(*home_page.Interactions)
        self.driver.execute_script("arguments[0].click();", interactions_link)
        # Creation of an Interactions Page instance
        interactions_page = InteractionsPage(self.driver)
        # scrolls down 30% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.3);")
        time.sleep(0.5)
        # Navigate to dragabble section
        interactions_page.click(*interactions_page.interactions_dragabble_section_button)
        # Asserting that the tittle of the section corresponds to Sortable
        interactions_page.assert_text(interactions_page.interactions_dragabble_section_title, "Dragabble")
        # Scrolls to the section title to enable better elements visibility
        section_title = interactions_page.find(*interactions_page.interactions_dragabble_section_title)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", section_title) 
        # Accessing the "Axis Restricted" section.
        interactions_page.click(*interactions_page.interactions_dragabble_axis_restricted_tab_button)
        # Attempting to move "Only X" both laterally and vertically
        interactions_page.drag_element(interactions_page.interactions_dragabble_axis_restricted_x_drag,
                                          150, 60)
        # Asserting the element only moved laterally
        element = interactions_page.find(*interactions_page.interactions_dragabble_axis_restricted_x_drag)
        element_style = element.get_attribute("style")
        assert "left: 150px" and "top: 0px" in element_style
        # Attempting to move "Only Y" both laterally and vertically
        interactions_page.drag_element(interactions_page.interactions_dragabble_axis_restricted_y_drag,
                                          100, 120)
        # Asserting the element only moved vertically
        element = interactions_page.find(*interactions_page.interactions_dragabble_axis_restricted_y_drag)
        element_style = element.get_attribute("style")
        assert "left: 0px" and "top: 120px" in element_style  
        
    def test_12_dragabble_container_restricted(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Interactions
        interactions_link = home_page.find(*home_page.Interactions)
        self.driver.execute_script("arguments[0].click();", interactions_link)
        # Creation of an Interactions Page instance
        interactions_page = InteractionsPage(self.driver)
        # scrolls down 30% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.3);")
        time.sleep(0.5)
        # Navigate to dragabble section
        interactions_page.click(*interactions_page.interactions_dragabble_section_button)
        # Asserting that the tittle of the section corresponds to Sortable
        interactions_page.assert_text(interactions_page.interactions_dragabble_section_title, "Dragabble")
        # Scrolls to the section title to enable better elements visibility
        section_title = interactions_page.find(*interactions_page.interactions_dragabble_section_title)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", section_title)
        time.sleep(1)
        # Accessing the "Container Restricted" section.
        interactions_page.click(*interactions_page.interactions_dragabble_container_restricted_tab_button)
        # Attempting to move the "box contained" element outside of the box and checking it is not possible
        # Obtaining containter's position and size
        container = interactions_page.find(*interactions_page.interactions_dragabble_container_restricted_container)
        container_location = container.location
        container_size = container.size
        container_left_limit = container_location['x']
        container_top_limit = container_location['y']
        container_right_limit = container_left_limit + container_size['width']
        container_bottom_limit = container_top_limit + container_size['height']
        # Attempting to move the element outside of the container to the bottom
        interactions_page.drag_element(interactions_page.interactions_dragabble_container_restricted_box_contained, 0, 150)
        element = interactions_page.find(*interactions_page.interactions_dragabble_container_restricted_box_contained)
        element_location = element.location
        #Checking the element has not moved outside of the container
        assert container_left_limit <= element_location['x'] <= container_right_limit, "The element has exceeded the left limit"
        assert container_top_limit <= element_location['y'] <= container_bottom_limit, "The element has exceeded the top limit"
        # Attempting to move the element outside of the container to the right
        interactions_page.drag_element(interactions_page.interactions_dragabble_container_restricted_box_contained, 500, 150)
        #Checking the element has not moved outside of the container
        assert container_left_limit <= element_location['x'] <= container_right_limit, "The element has exceeded the left limit"
        assert container_top_limit <= element_location['y'] <= container_bottom_limit, "The element has exceeded the top limit"
        # Attempting to move the element outside of the container to the top
        interactions_page.drag_element(interactions_page.interactions_dragabble_container_restricted_box_contained, 250, -150)
        #Checking the element has not moved outside of the container
        assert container_left_limit <= element_location['x'] <= container_right_limit, "The element has exceeded the left limit"
        assert container_top_limit <= element_location['y'] <= container_bottom_limit, "The element has exceeded the top limit"
        # Attempting to move the element outside of the container to the left
        interactions_page.drag_element(interactions_page.interactions_dragabble_container_restricted_box_contained, -50, 200)
        #Checking the element has not moved outside of the container
        assert container_left_limit <= element_location['x'] <= container_right_limit, "The element has exceeded the left limit"
        assert container_top_limit <= element_location['y'] <= container_bottom_limit, "The element has exceeded the top limit"
        # Scrolls to the "parent container" to enable better elements visibility
        parent_container = interactions_page.find(*interactions_page.interactions_dragabble_container_restricted_parent_container)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", parent_container)
        # Performing the same actions for the "parent contained" element inside the parent container
        container = interactions_page.find(*interactions_page.interactions_dragabble_container_restricted_parent_container)
        container_location = container.location
        container_size = container.size
        container_left_limit = container_location['x']
        container_top_limit = container_location['y']
        container_right_limit = container_left_limit + container_size['width']
        container_bottom_limit = container_top_limit + container_size['height']
        # Attempting to move the element outside of the container to the bottom
        interactions_page.drag_element(interactions_page.interactions_dragabble_container_restricted_parent_drag, 0, 150)
        element = interactions_page.find(*interactions_page.interactions_dragabble_container_restricted_parent_drag)
        element_location = element.location
        #Checking the element has not moved outside of the container
        assert container_left_limit <= element_location['x'] <= container_right_limit, "The element has exceeded the left limit"
        assert container_top_limit <= element_location['y'] <= container_bottom_limit, "The element has exceeded the top limit"
        # Attempting to move the element outside of the container to the right
        interactions_page.drag_element(interactions_page.interactions_dragabble_container_restricted_parent_drag, 150, 0)
        element = interactions_page.find(*interactions_page.interactions_dragabble_container_restricted_parent_drag)
        element_location = element.location
        #Checking the element has not moved outside of the container
        assert container_left_limit <= element_location['x'] <= container_right_limit, "The element has exceeded the left limit"
        assert container_top_limit <= element_location['y'] <= container_bottom_limit, "The element has exceeded the top limit" 
        # Attempting to move the element outside of the container to the top
        interactions_page.drag_element(interactions_page.interactions_dragabble_container_restricted_parent_drag, 0, -10)
        element = interactions_page.find(*interactions_page.interactions_dragabble_container_restricted_parent_drag)
        element_location = element.location
        #Checking the element has not moved outside of the container
        assert container_left_limit <= element_location['x'] <= container_right_limit, "The element has exceeded the left limit"
        assert container_top_limit <= element_location['y'] <= container_bottom_limit, "The element has exceeded the top limit"
        # Attempting to move the element outside of the container to the left
        interactions_page.drag_element(interactions_page.interactions_dragabble_container_restricted_parent_drag, -10, 0)
        element = interactions_page.find(*interactions_page.interactions_dragabble_container_restricted_parent_drag)
        element_location = element.location
        #Checking the element has not moved outside of the container
        assert container_left_limit <= element_location['x'] <= container_right_limit, "The element has exceeded the left limit"
        assert container_top_limit <= element_location['y'] <= container_bottom_limit, "The element has exceeded the top limit"  

    def test_13_dragabble_coursor_style(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Interactions
        interactions_link = home_page.find(*home_page.Interactions)
        self.driver.execute_script("arguments[0].click();", interactions_link)
        # Creation of an Interactions Page instance
        interactions_page = InteractionsPage(self.driver)
        # scrolls down 30% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.3);")
        time.sleep(0.5)
        # Navigate to dragabble section
        interactions_page.click(*interactions_page.interactions_dragabble_section_button)
        # Asserting that the tittle of the section corresponds to Sortable
        interactions_page.assert_text(interactions_page.interactions_dragabble_section_title, "Dragabble")
        # Scrolls to the section title to enable better elements visibility
        section_title = interactions_page.find(*interactions_page.interactions_dragabble_section_title)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", section_title)
        time.sleep(1)
        # Accessing the "Cursor Style" section.
        interactions_page.click(*interactions_page.interactions_dragabble_cursor_style_tab_button)

       
    
        
