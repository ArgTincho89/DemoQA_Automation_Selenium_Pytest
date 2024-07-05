from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.alerts_page import AlertsPage
from pages.home_page import HomePage
from tests.base_test import BaseTest



class TestAlerts(BaseTest):
    
    def test_01_browser_windows(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Alerts, Frame & Windows page
        alerts_link = home_page.find(*home_page.Alerts)
        self.driver.execute_script("arguments[0].click();", alerts_link)
        # Creation of an Alerts Page instance
        alerts_page = AlertsPage(self.driver)
        # Navigate to Browser Windows section
        alerts_page.click(*alerts_page.browser_windows_section_button)
        # Asserting that the tittle of the section corresponds to Browser Windows
        alerts_page.assert_text(alerts_page.browser_windows_section_title, "Browser Windows")
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        # Click the New Tab button
        alerts_page.click(*alerts_page.browser_windows_new_tab_button)
        original_tab = self.driver.current_window_handle
        # Wait for the new tab to be opened
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        # Switching to the new tab
        new_window = [window for window in self.driver.window_handles if window != original_tab][0]
        self.driver.switch_to.window(new_window)
        # Asserting the new tab has the correct URL
        assert self.driver.current_url == "https://demoqa.com/sample"
        # Closing the new tab and going back to the original tab
        self.driver.close()
        self.driver.switch_to.window(original_tab)
        # Click the New Window button
        alerts_page.click(*alerts_page.browser_windows_new_window_button)
        # Wait for the new window to be opened
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        # Switching to the new window
        new_window = [window for window in self.driver.window_handles if window != original_tab][0]
        self.driver.switch_to.window(new_window)
        # Asserting the new window has the correct URL
        assert self.driver.current_url == "https://demoqa.com/sample"
        # Closing the new window and going back to the original window
        self.driver.close()
        self.driver.switch_to.window(original_tab)
        # Click the New Window Message button
        alerts_page.click(*alerts_page.browser_windows_new_window_message_button)
        # Wait for the new window to be opened
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        # Store the original window 
        original_window = self.driver.current_window_handle
        # Identify the new window
        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        # Switch to the new window
        self.driver.switch_to.window(new_window)
        # Close the new window
        self.driver.close()
        # Switch back to the original window
        self.driver.switch_to.window(original_window)
 
    def test_02_alerts_test(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Alerts, Frame & Windows page
        alerts_link = home_page.find(*home_page.Alerts)
        self.driver.execute_script("arguments[0].click();", alerts_link)
        # Creation of an Alerts Page instance
        alerts_page = AlertsPage(self.driver)
        # Navigate to Alerts section
        alerts_page.click(*alerts_page.alerts_section_button)
        # Asserting that the tittle of the section corresponds to Browser Windows
        alerts_page.assert_text(alerts_page.alerts_section_title, "Alerts")
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        # Clicking the instant alert button and closing the alert
        alerts_page.click(*alerts_page.alert_instant_alert_button)
        # Wait for the alert to be present
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        # Switch to the alert
        alert = self.driver.switch_to.alert
        # Assert the text of the alert
        assert alert.text == "You clicked a button"
        # Accept the alert
        alert.accept()
        # Clicking the "will appear after 5 seconds" alert button
        alerts_page.click(*alerts_page.alert_five_seconds_alert_button)
        # Wait for the alert to be present
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        # Switch to the alert
        alert = self.driver.switch_to.alert
        # Assert the text of the alert
        assert alert.text == "This alert appeared after 5 seconds"
        # Accept the alert
        alert.accept()
        # Clicking the Confirm Box button
        alerts_page.click(*alerts_page.alert_confirm_box_button)
        # Wait for the alert to be present
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        # Switch to the alert
        alert = self.driver.switch_to.alert
        # Click "Accept"
        alert.accept()
        # Check the confirm message is correct
        alerts_page.assert_content_contains(alerts_page.alert_confirm_button_message, "Ok")
        # Clicking the Confirm Box button
        alerts_page.click(*alerts_page.alert_confirm_box_button)
        # Wait for the alert to be present
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        # Switch to the alert
        alert = self.driver.switch_to.alert
        # Click "Cancel"
        alert.dismiss()
        # Check the confirm message is correct
        alerts_page.assert_content_contains(alerts_page.alert_confirm_button_message, "Cancel")
        # Clicking the Prompt button
        alerts_page.click(*alerts_page.alert_prompt_button)
        # Wait for the alert to be present
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        # Switch to the alert
        alert = self.driver.switch_to.alert
        # Enter text into the prompt
        message = "Martin Miles's Selenium Pytest framework"
        alert.send_keys(message)
        # Click "Accept"
        alert.accept()
        # Checking that the promt is correctly displayed
        alerts_page.assert_content_contains(alerts_page.alert_prompt_result, message) 
        
    def test_03_frames_test(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Alerts, Frame & Windows page
        alerts_link = home_page.find(*home_page.Alerts)
        self.driver.execute_script("arguments[0].click();", alerts_link)
        # Creation of an Alerts Page instance
        alerts_page = AlertsPage(self.driver)
        # scrolls down 15% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.15);")
        # Navigate to Frames section
        alerts_page.click(*alerts_page.frames_section_button)
        # Asserting that the tittle of the section corresponds to Frames
        alerts_page.assert_text(alerts_page.frames_section_title, "Frames")
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        # Switching to iframe 1
        iframe1 = alerts_page.find(*alerts_page.frames_frame_1)
        self.driver.switch_to.frame(iframe1)
        # Asserting text in iframe 1
        alerts_page.assert_text(alerts_page.frames_fame_1_header, "This is a sample page")
        # Exiting the iframe
        self.driver.switch_to.default_content()
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        # Switching to iframe 2
        iframe2 = alerts_page.find(*alerts_page.frames_frame_2)
        self.driver.switch_to.frame(iframe2)
        # Asserting text in iframe 2
        alerts_page.assert_text(alerts_page.frames_fame_1_header, "This is a sample page")
        
    def test_04_nested_frames_test(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Alerts, Frame & Windows page
        alerts_link = home_page.find(*home_page.Alerts)
        self.driver.execute_script("arguments[0].click();", alerts_link)
        # Creation of an Alerts Page instance
        alerts_page = AlertsPage(self.driver)
        # scrolls down 15% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.15);")
        # Navigate to Nested Frames section
        alerts_page.click(*alerts_page.nested_frames_section_button)
        # Asserting that the tittle of the section corresponds to Nested Frames
        alerts_page.assert_text(alerts_page.nested_frames_section_title, "Nested Frames")
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        # Switching to Parent Frame
        parent_frame = alerts_page.find(*alerts_page.nested_frames_parent_frame)
        self.driver.switch_to.frame(parent_frame)
        # Asserting text "Parent frame" in parent frame's body
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Parent frame" in body_text
        # Switching to Child Frame
        child_frame = alerts_page.find(*alerts_page.nested_frames_child_frame)
        self.driver.switch_to.frame(child_frame)
        # Asserting text "Child Iframe" in Child frame's body
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Child Iframe" in body_text
        # Switching back to main content
        self.driver.switch_to.default_content()
        
    def test_05_modal_dialogs_tests(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Alerts, Frame & Windows page
        alerts_link = home_page.find(*home_page.Alerts)
        self.driver.execute_script("arguments[0].click();", alerts_link)
        # Creation of an Alerts Page instance
        alerts_page = AlertsPage(self.driver)
        # scrolls down 15% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.15);")
        # Navigate to Modal Dialogs section
        alerts_page.click(*alerts_page.modal_dialogs_section_button)
        # Asserting that the tittle of the section corresponds to Modal Dialogs
        alerts_page.assert_text(alerts_page.modal_dialogs_section_title, "Modal Dialogs")
        # Clicking the Small Modal button
        alerts_page.click(*alerts_page.modal_dialogs_small_modal_button)
        # Asserting content of small modal
        alerts_page.assert_content_contains(alerts_page.modal_dialogs_small_modal_content, "This is a small modal")
        # Clicking the close small modal button
        alerts_page.click(*alerts_page.modal_dialogs_small_modal_close_button)
        # Clicking the Large Modal button
        alerts_page.click(*alerts_page.modal_dialogs_large_modal_button)
        # Asserting the content of large modal
        alerts_page.assert_content_contains(alerts_page.modal_dialogs_large_modal_modal_content, "Lorem Ipsum")
        # Clicking the close large modal button
        alerts_page.click(*alerts_page.modal_dialogs_large_modal_close_button)
        