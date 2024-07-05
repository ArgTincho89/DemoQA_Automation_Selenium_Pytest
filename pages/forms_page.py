from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class FormsPage(BasePage):
    
    # Form elements locators
    forms_section_button = (By.CSS_SELECTOR, "div.left-pannel div.element-group:nth-of-type(2) div.element-list ul")
    forms_section_title = (By.CSS_SELECTOR, "h1.text-center")
    forms_first_name_field = (By.ID, "firstName")
    forms_last_name_field = (By.ID, "lastName")
    forms_email_field = (By.ID, "userEmail")
    forms_gender_male_button = (By.CSS_SELECTOR, "div.custom-control.custom-radio.custom-control-inline:nth-of-type(1) label")
    forms_gender_female_button = (By.CSS_SELECTOR, "div.custom-control.custom-radio.custom-control-inline:nth-of-type(2) label")
    forms_gender_other_button = (By.CSS_SELECTOR, "div.custom-control.custom-radio.custom-control-inline:nth-of-type(3) label")
    forms_mobile_number_field = (By.ID, "userNumber")
    forms_dob_field = (By.ID, "dateOfBirthInput")
    forms_dob_month_picker = (By.CSS_SELECTOR, "#dateOfBirth > div.react-datepicker__tab-loop > div.react-datepicker-popper > div > div > div.react-datepicker__month-container > div.react-datepicker__header > div.react-datepicker__header__dropdown.react-datepicker__header__dropdown--select > div.react-datepicker__month-dropdown-container.react-datepicker__month-dropdown-container--select > select")
    forms_dob_month_august = (By.CSS_SELECTOR, "#dateOfBirth > div.react-datepicker__tab-loop > div.react-datepicker-popper > div > div > div.react-datepicker__month-container > div.react-datepicker__header > div.react-datepicker__header__dropdown.react-datepicker__header__dropdown--select > div.react-datepicker__month-dropdown-container.react-datepicker__month-dropdown-container--select > select > option[value='7']")
    forms_dob_day_28 = (By.CSS_SELECTOR, "#dateOfBirth > div.react-datepicker__tab-loop > div.react-datepicker-popper > div > div > div.react-datepicker__month-container > div.react-datepicker__month > div:nth-child(5) > div.react-datepicker__day.react-datepicker__day--028")
    forms_dob_year_picker = (By.CSS_SELECTOR, "#dateOfBirth > div.react-datepicker__tab-loop > div.react-datepicker-popper > div > div > div.react-datepicker__month-container > div.react-datepicker__header > div.react-datepicker__header__dropdown.react-datepicker__header__dropdown--select > div.react-datepicker__year-dropdown-container.react-datepicker__year-dropdown-container--select > select")
    forms_dob_year_1989 = (By.CSS_SELECTOR, "#dateOfBirth > div.react-datepicker__tab-loop > div.react-datepicker-popper > div > div > div.react-datepicker__month-container > div.react-datepicker__header > div.react-datepicker__header__dropdown.react-datepicker__header__dropdown--select > div.react-datepicker__year-dropdown-container.react-datepicker__year-dropdown-container--select > select > option[value='1989']")
    forms_subjects_field = (By.CSS_SELECTOR, "div#subjectsWrapper div:nth-of-type(2) input")
    forms_subjects_tag = (By.CSS_SELECTOR, "#subjectsContainer div div div div")
    forms_hobbies_sports_checkbox = (By.CSS_SELECTOR, "div.custom-control.custom-checkbox.custom-control-inline:nth-of-type(1) label")
    forms_hobbies_reading_checkbox = (By.CSS_SELECTOR, "div.custom-control.custom-checkbox.custom-control-inline:nth-of-type(2) label")
    forms_hobbies_music_checkbox = (By.CSS_SELECTOR, "div.custom-control.custom-checkbox.custom-control-inline:nth-of-type(3) label")
    forms_upload_picture_button = (By.ID, "uploadPicture")
    forms_upload_path = (By.CSS_SELECTOR, "div.form-file input")
    forms_current_address_field = (By.ID, "currentAddress")
    forms_state_field = (By.CSS_SELECTOR, "#state div div div svg")
    forms_selected_state = (By.CSS_SELECTOR, "#state div div div")
    forms_city_field = (By.ID, "city")
    forms_selected_city = (By.CSS_SELECTOR, "#city div div div")
    forms_submit_button = (By.ID, "submit")
    forms_submited_name = (By.CSS_SELECTOR, "body > div.fade.modal.show > div > div > div.modal-body > div > table > tbody > tr:nth-child(1) > td:nth-child(2)")
    forms_submited_email = (By.CSS_SELECTOR, "body > div.fade.modal.show > div > div > div.modal-body > div > table > tbody > tr:nth-child(2) > td:nth-child(2)")
    forms_submited_gender = (By.CSS_SELECTOR, "body > div.fade.modal.show > div > div > div.modal-body > div > table > tbody > tr:nth-child(3) > td:nth-child(2)")
    forms_submited_mobile = (By.CSS_SELECTOR, "body > div.fade.modal.show > div > div > div.modal-body > div > table > tbody > tr:nth-child(4) > td:nth-child(2)")
    forms_submited_dob = (By.CSS_SELECTOR, "body > div.fade.modal.show > div > div > div.modal-body > div > table > tbody > tr:nth-child(5) > td:nth-child(2)")
    forms_submited_subjects = (By.CSS_SELECTOR, "body > div.fade.modal.show > div > div > div.modal-body > div > table > tbody > tr:nth-child(6) > td:nth-child(2)")
    forms_submited_hobbies = (By.CSS_SELECTOR, "body > div.fade.modal.show > div > div > div.modal-body > div > table > tbody > tr:nth-child(7) > td:nth-child(2)")
    forms_submited_picture = (By.CSS_SELECTOR, "body > div.fade.modal.show > div > div > div.modal-body > div > table > tbody > tr:nth-child(8) > td:nth-child(2)")
    forms_submited_address = (By.CSS_SELECTOR, "body > div.fade.modal.show > div > div > div.modal-body > div > table > tbody > tr:nth-child(9) > td:nth-child(2)")
    
    
    
    def __init__(self, driver):
        super().__init__(driver)