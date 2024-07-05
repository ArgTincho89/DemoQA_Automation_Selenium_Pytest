import os
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.elements_page import ElementsPage
from pages.home_page import HomePage
from tests.base_test import BaseTest



class TestElements(BaseTest):
    
    def test_01_Complete_Text_Box_Fields(self):
        # Accessing to the Text Box section, completing the form, submitting and asserting results
        home_page = HomePage(self.driver)
        # Navigate to Elements page
        elements_link = home_page.find(*home_page.Elements)
        self.driver.execute_script("arguments[0].click();", elements_link)
        # Creation of an Elements Page instance
        elements_page = ElementsPage(self.driver)
        # Navigate to Text Box section
        text_box_section_button = elements_page.find(*elements_page.text_box_section_button)
        text_box_section_button.click() 
        # Asserting that the tittle of the section corresponds to Text Box
        elements_page.assert_text(elements_page.text_box_section_title, "Text Box")
        # Complete Full Name Field
        elements_page.set(elements_page.full_name_field, "John Doe")
        # Complete Email Address Field
        elements_page.set(elements_page.email_field, "johndoe@gmail.com")
        # Complete Current Address field
        elements_page.set(elements_page.current_address, "Address 123")
         # Complete Permanent Address field
        elements_page.set(elements_page.permanent_address, "Address 456")
        # Scroll down to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Click Submit button
        submit_button = elements_page.find(*elements_page.text_box_submit_button)
        submit_button.click()
        # Check that the data was correctly submited by asserting the form response
        elements_page.assert_content_contains(elements_page.registered_name_field, "John Doe")
        elements_page.assert_content_contains(elements_page.registered_email_field, "johndoe@gmail.com")
        elements_page.assert_content_contains(elements_page.registered_current_address_field, "Address 123")
        elements_page.assert_content_contains(elements_page.registered_permanent_address_field, "Address 456")
        self.driver.close
        
    def test_02_check_box_section(self):
        # Interacting with the elements of the check box section
        home_page = HomePage(self.driver)
        # Navigate to Elements page
        elements_link = home_page.find(*home_page.Elements)
        self.driver.execute_script("arguments[0].click();", elements_link)
        # Creation of an Elements Page instance
        elements_page = ElementsPage(self.driver)
        # Navigate to check Box section
        check_box_section_button = elements_page.find(*elements_page.check_box_section_button)
        check_box_section_button.click()
        # Asserting that the tittle of the section corresponds to Check Box
        elements_page.assert_text(elements_page.check_box_section_title, "Check Box")
        # Checking that, when clicking the Expand All button, all the elements are displayed
        elements_page.click(*elements_page.button_expand_all)
        elements_page.assert_element_visibility(elements_page.home_check_box)
        elements_page.assert_element_visibility(elements_page.desktop_check_box)
        elements_page.assert_element_visibility(elements_page.desktop_notes_checkbox)
        elements_page.assert_element_visibility(elements_page.desktop_commands_checkbox)
        elements_page.assert_element_visibility(elements_page.documents_check_box)
        elements_page.assert_element_visibility(elements_page.documents_workspace_checkbox)
        elements_page.assert_element_visibility(elements_page.documents_workspace_react_checkbox)
        elements_page.assert_element_visibility(elements_page.documents_workspace_angular_checkbox)
        elements_page.assert_element_visibility(elements_page.documents_workspace_vue_checkbox)
        elements_page.assert_element_visibility(elements_page.documents_office_checkbox)
        elements_page.assert_element_visibility(elements_page.documents_office_public_checkbox)
        elements_page.assert_element_visibility(elements_page.documents_office_private_checkbox)
        elements_page.assert_element_visibility(elements_page.documents_office_classified_checkbox)
        elements_page.assert_element_visibility(elements_page.documents_office_general_checkbox)
        elements_page.assert_element_visibility(elements_page.downloads_check_box)
        elements_page.assert_element_visibility(elements_page.downloads_wordfile_checkbox)
        elements_page.assert_element_visibility(elements_page.downloads_excelfile_checkbox)
        # Checking that when clicking the Collapse All button, all the elements are hidden, except for Home
        elements_page.click(*elements_page.button_collapse_all)
        elements_page.assert_element_visibility(elements_page.home_check_box)
        elements_page.assert_element_not_present(elements_page.desktop_check_box)
        elements_page.assert_element_not_present(elements_page.desktop_notes_checkbox)
        elements_page.assert_element_not_present(elements_page.desktop_commands_checkbox)
        elements_page.assert_element_not_present(elements_page.documents_check_box)
        elements_page.assert_element_not_present(elements_page.documents_workspace_checkbox)
        elements_page.assert_element_not_present(elements_page.documents_workspace_react_checkbox)
        elements_page.assert_element_not_present(elements_page.documents_workspace_angular_checkbox)
        elements_page.assert_element_not_present(elements_page.documents_workspace_vue_checkbox)
        elements_page.assert_element_not_present(elements_page.documents_office_checkbox)
        elements_page.assert_element_not_present(elements_page.documents_office_public_checkbox)
        elements_page.assert_element_not_present(elements_page.documents_office_private_checkbox)
        elements_page.assert_element_not_present(elements_page.documents_office_classified_checkbox)
        elements_page.assert_element_not_present(elements_page.documents_office_general_checkbox)
        elements_page.assert_element_not_present(elements_page.downloads_check_box)
        elements_page.assert_element_not_present(elements_page.downloads_wordfile_checkbox)
        elements_page.assert_element_not_present(elements_page.downloads_excelfile_checkbox)
        # Clicking each check box and asserting that the results correctly displays the adherence
        elements_page.click(*elements_page.home_expand_button)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scrolls down to avoid adds intercepting clicks
        elements_page.click(*elements_page.desktop_check_box)
        elements_page.assert_content_contains(elements_page.check_box_results, "desktop", "notes", "commands")
        elements_page.click(*elements_page.documents_check_box)
        elements_page.assert_content_contains(elements_page.check_box_results, "documents", "workspace", "react",
                                              "angular", "veu", "office", "public", "private", "classified", "general")
        elements_page.click(*elements_page.downloads_check_box)
        elements_page.assert_content_contains(elements_page.check_box_results, "downloads", "wordFile", "excelFile")
        self.driver.close
        
    def test_03_radio_button_tests(self):
        # Interacting with the Radio Button elements section.
        home_page = HomePage(self.driver)
        # Navigate to Elements page
        elements_link = home_page.find(*home_page.Elements)
        self.driver.execute_script("arguments[0].click();", elements_link)
        # Creation of an Elements Page instance
        elements_page = ElementsPage(self.driver)
        # Navigate to Radio Button section
        elements_page.click(*elements_page.radio_button_section_button)
        # Asserting that the tittle of the section corresponds to Radio Button
        elements_page.assert_text(elements_page.radio_button_section_title, "Radio Button")
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")# scrolls down a 20% to enable better visibility of elements
        # Selecting the "Yes" option and asserting the correct response
        elements_page.click(*elements_page.radio_button_yes_button)
        elements_page.assert_content_contains(elements_page.radio_button_selection_result, "Yes")
        # Selecting the "Impressive" option and asserting the correct response
        elements_page.click(*elements_page.radio_button_impressive_button)
        elements_page.assert_content_contains(elements_page.radio_button_selection_result, "Impressive")
        # Checks that the "No" option is disabled
        radio_button_no_option = elements_page.find(*elements_page.radio_button_no_option)
        assert "disabled" in radio_button_no_option.get_attribute("class")
        
    def test_04_web_tables_tests(self):
        # Interacting with the elements of the Web Tables section.
        home_page = HomePage(self.driver)
        # Navigate to Elements page
        elements_link = home_page.find(*home_page.Elements)
        self.driver.execute_script("arguments[0].click();", elements_link)
        # Creation of an Elements Page instance
        elements_page = ElementsPage(self.driver)
        # Navigate to web tables section
        elements_page.click(*elements_page.web_tables_section_button)
        # Asserting that the tittle of the section corresponds to Web Tables
        elements_page.assert_text(elements_page.web_tables_section_title, "Web Tables")
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        # Adding a new element to the table
        elements_page.click(*elements_page.web_tables_add_button)
        elements_page.set(elements_page.web_tables_registration_firstname_field, "zzzz")
        elements_page.set(elements_page.web_tables_registration_lastname_field, "yyyy")
        elements_page.set(elements_page.web_tables_registration_email_field, "zzzzyyyy@gmail.com")
        elements_page.set(elements_page.web_tables_registration_age_field, "50")
        elements_page.set(elements_page.web_tables_registration_salary_field, "50000")
        elements_page.set(elements_page.web_tables_registration_department_field, "Quality Assurance")
        elements_page.click(*elements_page.web_tables_registration_submit_button)
        # Checking that the First Name column correctly orders the content in ascending/descending order when clicking the header
        first_name_list = []
        for i in range(1, 5):
            element = self.driver.find_element(By.CSS_SELECTOR, f"div.rt-tr-group:nth-of-type({i}) div.rt-td:nth-of-type(1)").text
            first_name_list.append(element)
            
        elements_page.click(*elements_page.web_tables_firstname_header)
        
        first_name_ascending = []
        for i in range(1, 5):
            element = self.driver.find_element(By.CSS_SELECTOR, f"div.rt-tr-group:nth-of-type({i}) div.rt-td:nth-of-type(1)").text
            first_name_ascending.append(element)
        assert sorted(first_name_list) == first_name_ascending
        # Checking reverse order is correct
        elements_page.click(*elements_page.web_tables_firstname_header)
        
        first_name_descending= []
        for i in range(1, 5):
            element = self.driver.find_element(By.CSS_SELECTOR, f"div.rt-tr-group:nth-of-type({i}) div.rt-td:nth-of-type(1)").text
            first_name_descending.append(element)
        assert sorted(first_name_list, reverse = True) == first_name_descending
        
        # Checking that the last Name column correctly orders the content in ascending/descending order when clicking the header
        last_name_list = []
        for i in range(1, 5):
            element = self.driver.find_element(By.CSS_SELECTOR, f"div.rt-tr-group:nth-of-type({i}) div.rt-td:nth-of-type(2)").text
            last_name_list.append(element)
            
        elements_page.click(*elements_page.web_tables_lastname_header)
        
        last_name_ascending = []
        for i in range(1, 5):
            element = self.driver.find_element(By.CSS_SELECTOR, f"div.rt-tr-group:nth-of-type({i}) div.rt-td:nth-of-type(2)").text
            last_name_ascending.append(element)
        assert sorted(last_name_list) == last_name_ascending
        # Checking reverse order is correct
        elements_page.click(*elements_page.web_tables_lastname_header)
        
        last_name_descending= []
        for i in range(1, 5):
            element = self.driver.find_element(By.CSS_SELECTOR, f"div.rt-tr-group:nth-of-type({i}) div.rt-td:nth-of-type(2)").text
            last_name_descending.append(element)
        assert sorted(last_name_list, reverse = True) == last_name_descending
        
        # Checking that the Age column correctly orders the content in ascending/descending order when clicking the header.
        age_list = []
        for i in range(1, 5):
            element = self.driver.find_element(By.CSS_SELECTOR, f"div.rt-tr-group:nth-of-type({i}) div.rt-td:nth-of-type(3)").text
            age_list.append(element)
            
        elements_page.click(*elements_page.web_tables_age_header)
        
        age_ascending = []
        for i in range(1,5):
            element = self.driver.find_element(By.CSS_SELECTOR, f"div.rt-tr-group:nth-of-type({i}) div.rt-td:nth-of-type(3)").text
            age_ascending.append(element)
        assert sorted(age_list) == age_ascending
        # Checking reverse order is correct
        elements_page.click(*elements_page.web_tables_age_header)
        
        age_descending = []
        for i in range(1,5):
            element = self.driver.find_element(By.CSS_SELECTOR, f"div.rt-tr-group:nth-of-type({i}) div.rt-td:nth-of-type(3)").text
            age_descending.append(element)
        assert sorted(age_list, reverse=True) == age_descending
        
        # Checking that the Email column correctly orders the content in ascending/descending order when clicking the header.
        email_list = []
        for i in range(1, 5):
            element = self.driver.find_element(By.CSS_SELECTOR, f"div.rt-tr-group:nth-of-type({i}) div.rt-td:nth-of-type(4)").text
            email_list.append(element)
            
        elements_page.click(*elements_page.web_tables_email_header)
        
        email_ascending = []
        for i in range(1, 5):
            element = self.driver.find_element(By.CSS_SELECTOR, f"div.rt-tr-group:nth-of-type({i}) div.rt-td:nth-of-type(4)").text
            email_ascending.append(element)
        assert sorted(email_list) == email_ascending
        # Checking reverse order is correct
        elements_page.click(*elements_page.web_tables_email_header)
        
        email_descending = []
        for i in range(1, 5):
            element = self.driver.find_element(By.CSS_SELECTOR, f"div.rt-tr-group:nth-of-type({i}) div.rt-td:nth-of-type(4)").text
            email_descending.append(element)
        assert sorted(email_list, reverse=True) == email_descending
        
        # Checking that the Email column correctly orders the content in ascending/descending order when clicking the header.
        salary_list = []
        for i in range(1, 5):
            element = self.driver.find_element(By.CSS_SELECTOR, f"div.rt-tr-group:nth-of-type({i}) div.rt-td:nth-of-type(5)").text
            salary_list.append(int(element))
            
        elements_page.click(*elements_page.web_tables_salary_header)
        
        salary_ascending = []
        for i in range(1, 5):
            element = self.driver.find_element(By.CSS_SELECTOR, f"div.rt-tr-group:nth-of-type({i}) div.rt-td:nth-of-type(5)").text
            salary_ascending.append(int(element))
        assert sorted(salary_list) == salary_ascending
        
        # Checking reverse order is correct
        elements_page.click(*elements_page.web_tables_salary_header)
        
        salary_descending = []
        for i in range(1, 5):
            element = self.driver.find_element(By.CSS_SELECTOR, f"div.rt-tr-group:nth-of-type({i}) div.rt-td:nth-of-type(5)").text
            salary_descending.append(int(element))
        assert sorted(salary_list, reverse=True) == salary_descending
        
        # Checking that the Department column correctly orders the content in ascending/descending order when clicking the header.
        department_list = []
        for i in range(1, 5):
            element = self.driver.find_element(By.CSS_SELECTOR, f"div.rt-tr-group:nth-of-type({i}) div.rt-td:nth-of-type(6)").text
            department_list.append(element)
            
        elements_page.click(*elements_page.web_tables_department_header)
        
        department_ascending = []
        for i in range(1, 5):
            element = self.driver.find_element(By.CSS_SELECTOR, f"div.rt-tr-group:nth-of-type({i}) div.rt-td:nth-of-type(6)").text
            department_ascending.append(element)
        assert sorted(department_list) == department_ascending
        # Checking reverse order is correct
        elements_page.click(*elements_page.web_tables_department_header)
        
        department_descending = []
        for i in range(1, 5):
            element = self.driver.find_element(By.CSS_SELECTOR, f"div.rt-tr-group:nth-of-type({i}) div.rt-td:nth-of-type(6)").text
            department_descending.append(element)
        assert sorted(department_list, reverse=True) == department_descending

        # Editing the information of a user
        elements_page.click(*elements_page.web_tables_elementone_edit_button)
        elements_page.set(elements_page.web_tables_registration_firstname_field, "zzzz-edited")
        elements_page.set(elements_page.web_tables_registration_lastname_field, "yyyy-edited")
        elements_page.set(elements_page.web_tables_registration_email_field, "zzzzyyyy-edited@gmail.com")
        elements_page.set(elements_page.web_tables_registration_age_field, "99")
        elements_page.set(elements_page.web_tables_registration_salary_field, "50001")
        elements_page.set(elements_page.web_tables_registration_department_field, "Quality Assurance-edited")
        elements_page.click(*elements_page.web_tables_registration_submit_button)
        # Searching for the recently edited user by performing a search in the search box
        elements_page.set(elements_page.web_tables_search_input, "edited")
        # Asserting the recently performed changes to the user's data
        elements_page.assert_text(elements_page.web_tables_firstname_field, "zzzz-edited")
        elements_page.assert_text(elements_page.web_tables_lastname_field, "yyyy-edited")
        elements_page.assert_text(elements_page.web_tables_email_field, "zzzzyyyy-edited@gmail.com")
        elements_page.assert_text(elements_page.web_tables_age_field, "99")
        elements_page.assert_text(elements_page.web_tables_salary_field, "50001")
        elements_page.assert_text(elements_page.web_tables_department_field, "Quality Assurance-edited")
        # Deleting the created user
        elements_page.click(*elements_page.web_tables_elementone_delete_button)
        # Checking that the user was correctly deleted
        elements_page.set(elements_page.web_tables_search_input, "edited")
        searched_user = elements_page.find(*elements_page.web_tables_firstname_field).text
        assert searched_user.strip() == "" 
        
    def test_05_buttons_tests(self):
        # Interacting with the elements of the buttons section.
        home_page = HomePage(self.driver)
        # Navigate to Elements page
        elements_link = home_page.find(*home_page.Elements)
        self.driver.execute_script("arguments[0].click();", elements_link)
        # Creation of an Elements Page instance
        elements_page = ElementsPage(self.driver)
        # Navigate to buttons section
        elements_page.click(*elements_page.buttons_section_button)
        time.sleep(0.5) # Wait for the screen to adopt correct size
        # Asserting that the tittle of the section corresponds to Buttons
        elements_page.assert_text(elements_page.buttons_section_title, "Buttons")
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        time.sleep(0.5) # Wait for the screen to adopt correct size
        # Performing a Double Click on the Double Click button and asserting the correct response message
        elements_page.double_click(*elements_page.buttons_double_click_button)
        elements_page.assert_text(elements_page.buttons_double_click_message, "You have done a double click")
        # Performing a Right Click on the Right Click button and asserting the correct response message
        elements_page.right_click(*elements_page.buttons_right_click_button)
        elements_page.assert_text(elements_page.buttons_right_click_message, "You have done a right click")
        # Performing a click on the Click me button and asserting the correct response message
        elements_page.click(*elements_page.buttons_click_button)
        elements_page.assert_text(elements_page.buttons_click_message, "You have done a dynamic click") 
        
    def test_06_links_tests(self):
        # Interacting with the elements of the links section.
        home_page = HomePage(self.driver)
        # Navigate to Elements page
        elements_link = home_page.find(*home_page.Elements)
        self.driver.execute_script("arguments[0].click();", elements_link)
        # Creation of an Elements Page instance
        elements_page = ElementsPage(self.driver)
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        # Navigate to Links section
        elements_page.click(*elements_page.links_section_button)
        time.sleep(0.5) # Wait for the screen to adopt correct size
        # Asserting that the tittle of the section corresponds to Links
        elements_page.assert_text(elements_page.links_section_title, "Links")
        # scrolls down 30% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.3);")
        # Click Home link, check the url and close the tab
        elements_page.click(*elements_page.links_home_link)
        original_tab = self.driver.current_window_handle
        # Wait for the new tab to be opened
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        # Switching to the new tab
        new_window = [window for window in self.driver.window_handles if window != original_tab][0]
        self.driver.switch_to.window(new_window)
        # Asserting the new tab has the correct URL
        assert self.driver.current_url == "https://demoqa.com/"
        # Closing the new tab and going back to the original tab
        self.driver.close()
        self.driver.switch_to.window(original_tab)
        # scrolls down 15% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.15);")
        # Checking that the "Created" link, sends the correct API call
        elements_page.click(*elements_page.links_created_link)
        elements_page.assert_content_contains(elements_page.links_results, "201", "Created")
        # Checking that the "No Content" link, sends the correct API call
        elements_page.click(*elements_page.links_no_content_link)
        time.sleep(0.1) 
        elements_page.assert_content_contains(elements_page.links_results, "204", "No Content")
        # Checking that the "Moved" link, sends the correct API call
        elements_page.click(*elements_page.links_moved_link)
        time.sleep(0.1)
        elements_page.assert_content_contains(elements_page.links_results, "301", "Moved Permanently")
        # Checking that the "Bad Request" link, sends the correct API call
        elements_page.click(*elements_page.links_bad_request_link)
        time.sleep(0.1)
        elements_page.assert_content_contains(elements_page.links_results, "400", "Bad Request")
        # Checking that the "Unauthorized" link, sends the correct API call
        elements_page.click(*elements_page.links_unauthorized_link)
        time.sleep(0.1)
        elements_page.assert_content_contains(elements_page.links_results, "401", "Unauthorized")
        # Checking that the "Forbidden" link, sends the correct API call
        elements_page.click(*elements_page.links_forbidden_link)
        time.sleep(0.1)
        elements_page.assert_content_contains(elements_page.links_results, "403", "Forbidden")
        # Checking that the "Not Found" link, sends the correct API call
        elements_page.click(*elements_page.links_not_found_link)
        time.sleep(0.1)
        elements_page.assert_content_contains(elements_page.links_results, "404", "Not Found") 
        
    def test_07_upload_and_download_files_test(self):
        # Interacting with the elements of the Upload and Download section.
        home_page = HomePage(self.driver)
        # Navigate to Elements page
        elements_link = home_page.find(*home_page.Elements)
        self.driver.execute_script("arguments[0].click();", elements_link)
        # Creation of an Elements Page instance
        elements_page = ElementsPage(self.driver)
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        # Navigate to Upload and download section
        elements_page.click(*elements_page.upload_section_button)
        time.sleep(0.5) # Wait for the screen to adopt correct size
        # Asserting that the tittle of the section corresponds to Upload and Download
        elements_page.assert_text(elements_page.upload_section_title, "Upload and Download")
        # scrolls down 15% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.15);")
        # Uploading a file located in the utilities folder
        file_path = "C:\\Users\\marti\\OneDrive\\Escritorio\\Martin\\Selenium\\DemoQA_tests\\utilities\\softwaretesting.jpg"
        elements_page.upload_file(elements_page.upload_button, file_path)
        # Checking that the path message contains the name of the file
        elements_page.assert_content_contains(elements_page.upload_uploaded_file_path, "softwaretesting")
        # Click on the download button
        elements_page.click(*elements_page.download_button)
        # Wait for the file to download
        time.sleep(5)  # Adjust this time based on your internet speed and file size
        # Verify the file has been downloaded
        download_path = "C:\\Users\\marti\\Downloads\\DemoQADownloads" 
        # Lists all files in the download path
        files_in_download_dir = os.listdir(download_path)
        # Filter the files that contain 'sampleFile' in the name and has the '.jpeg' format.
        matching_files = [file for file in files_in_download_dir if 'sampleFile' in file and file.endswith('.jpeg')]
        # Checking that the file is found
        assert len(matching_files) > 0, "No file containing 'sampleFile' and of format 'jpeg' has been found."  
        
    def test_08_dynamic_properties_tests(self):
        # Interacting with the elements of the links section.
        home_page = HomePage(self.driver)
        # Navigate to Elements page
        elements_link = home_page.find(*home_page.Elements)
        self.driver.execute_script("arguments[0].click();", elements_link)
        # Creation of an Elements Page instance
        elements_page = ElementsPage(self.driver)
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        # Navigate to Dynamic Properties section
        elements_page.click(*elements_page.dynamic_properties_section_button)
        time.sleep(0.5) # Wait for the screen to adopt correct size
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        # Asserting that the tittle of the section corresponds to Dynamic Properties
        elements_page.assert_text(elements_page.dynamic_properties_section_title, "Dynamic Properties")
        # Locating the Random Id text
        elements_page.find(*elements_page.dynamic_properties_random_id_text)
        # Checking that the "Will enable 5 seconds" button is disabled
        enable_button = elements_page.find(*elements_page.dynamic_properties_enable_button)
        assert not enable_button.is_enabled()
        # Checking that the "Color Change" button text's color is white
        color_change_button = elements_page.find(*elements_page.dynamic_properties_color_change_button)
        color_text = color_change_button.value_of_css_property("color")
        expected_color_white = "rgba(255, 255, 255, 1)" 
        assert color_text == expected_color_white
        # Waiting for the "Visible After 5 Seconds" button
        elements_page.find(*elements_page.dynamic_properties_visible_after_button)
        # Checking that the "Will enable 5 seconds" button is now enabled
        assert enable_button.is_enabled()
        # Checking that the "Color Change" button text's color is now #dc3545
        color_text_after = color_change_button.value_of_css_property("color")
        expected_color_dc3545 = "rgba(220, 53, 69, 1)" 
        assert color_text_after == expected_color_dc3545