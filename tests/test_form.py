from selenium.webdriver.common.keys import Keys
from pages.forms_page import FormsPage
from pages.home_page import HomePage
from tests.base_test import BaseTest



class TestForm(BaseTest):
    
    def test_01_Complete_form_test(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Forms page
        forms_link = home_page.find(*home_page.Forms)
        self.driver.execute_script("arguments[0].click();", forms_link)
        # Creation of an Forms Page instance
        forms_page = FormsPage(self.driver)
        # Navigate to Practice Form section
        practice_form_section_button = forms_page.find(*forms_page.forms_section_button)
        practice_form_section_button.click()
        # Fill in the form's fields
        firstName = "John"
        lastName = "Doe"
        email = "johndoe@email.com"
        phone = "1234567890"
        currentAddress = "742 Evergreen Terrace"
        forms_page.set(forms_page.forms_first_name_field, firstName)
        forms_page.set(forms_page.forms_last_name_field, lastName)
        forms_page.set(forms_page.forms_email_field, email)
        forms_page.set(forms_page.forms_mobile_number_field, phone)
        forms_page.set(forms_page.forms_current_address_field, currentAddress)
        # Fill in Subjects field and assert correct results
        forms_page.set(forms_page.forms_subjects_field, "comp")
        subject_field = forms_page.find(*forms_page.forms_subjects_field)
        subject_field.send_keys(Keys.DOWN, Keys.ENTER)
        forms_page.assert_content_contains(forms_page.forms_subjects_tag, "Computer Science")
        # Select Gender
        forms_page.click(*forms_page.forms_gender_male_button)
        # Select a hobbie
        forms_page.click(*forms_page.forms_hobbies_sports_checkbox)
        # Selecting Date of Birth
        forms_page.click(*forms_page.forms_dob_field)
        forms_page.click(*forms_page.forms_dob_month_picker)
        forms_page.click(*forms_page.forms_dob_month_august)
        forms_page.click(*forms_page.forms_dob_year_picker)
        forms_page.click(*forms_page.forms_dob_year_1989)
        forms_page.click(*forms_page.forms_dob_day_28)
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        # Upload Picture
        file_path = "C:\\Users\\marti\\OneDrive\\Escritorio\\Martin\\Selenium\\DemoQA_tests\\utilities\\softwaretesting.jpg"
        forms_page.upload_file(forms_page.forms_upload_picture_button, file_path)
        # Selecting State and City
        """forms_page.click(*forms_page.forms_state_field)
        state_field = forms_page.find(*forms_page.forms_state_field)
        time.sleep(1)
        state_field.send_keys(Keys.ENTER)
        time.sleep(2)
        forms_page.assert_text(forms_page.forms_city_field, "NCR")
        forms_page.click(*forms_page.forms_city_field)
        city_field = forms_page.find(*forms_page.forms_city_field)
        city_field.send_keys(Keys.ENTER)
        forms_page.assert_text(forms_page.forms_selected_city, "Delhi")"""
        # Click Submit button
        forms_page.click(*forms_page.forms_submit_button)
        # Asserting the correct information has been submited
        forms_page.assert_text(forms_page.forms_submited_name, "John Doe")
        forms_page.assert_text(forms_page.forms_submited_email, email)
        forms_page.assert_text(forms_page.forms_submited_gender, "Male")
        forms_page.assert_text(forms_page.forms_submited_mobile, phone)
        forms_page.assert_text(forms_page.forms_submited_dob, "28 August,1989")
        forms_page.assert_text(forms_page.forms_submited_subjects, "Computer Science")
        forms_page.assert_text(forms_page.forms_submited_hobbies, "Sports")
        forms_page.assert_text(forms_page.forms_submited_picture, "softwaretesting.jpg")
        forms_page.assert_text(forms_page.forms_submited_address, currentAddress)
        
         