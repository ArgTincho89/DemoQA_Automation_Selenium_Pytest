
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ElementsPage(BasePage):
    
    # Text Box elements locators
    text_box_section_button = (By.CSS_SELECTOR, "div.element-group:nth-of-type(1) #item-0")
    text_box_section_title = (By.CSS_SELECTOR, "h1.text-center")
    full_name_field = (By.CSS_SELECTOR, "div#userName-wrapper input")
    email_field = (By.CSS_SELECTOR, "div#userEmail-wrapper input")
    current_address = (By.CSS_SELECTOR, "div#currentAddress-wrapper textarea")
    permanent_address = (By.CSS_SELECTOR, "textarea#permanentAddress")
    text_box_submit_button = (By.ID, "submit")
    registered_name_field = (By.ID, "name")
    registered_email_field = (By.ID, "email")
    registered_current_address_field = (By.CSS_SELECTOR, "p#currentAddress")
    registered_permanent_address_field = (By.CSS_SELECTOR, "p#permanentAddress")
    
    # Check Box elements locators
    check_box_section_button  = (By.CSS_SELECTOR, "div.element-group:nth-of-type(1) #item-1")
    check_box_section_title = (By.CSS_SELECTOR, "h1.text-center")
    button_expand_all = (By.CSS_SELECTOR, "button[title='Expand all']")
    button_collapse_all = (By.CSS_SELECTOR, "button[title='Collapse all']")
    home_check_box = (By.CSS_SELECTOR, "#tree-node > ol > li > span > label > span.rct-checkbox > svg")
    desktop_check_box = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(1) > span > label > span.rct-checkbox > svg")
    desktop_notes_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(1) > span > label > span.rct-checkbox")
    desktop_commands_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(2) > span > label > span.rct-checkbox")
    documents_check_box = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > span > label > span.rct-checkbox > svg")
    documents_workspace_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(1) > span > label > span.rct-checkbox")
    documents_workspace_react_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(1) > span > label > span.rct-checkbox > svg")
    documents_workspace_angular_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(2) > span > label > span.rct-checkbox > svg")
    documents_workspace_vue_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(3) > span > label > span.rct-checkbox > svg")
    documents_office_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(2) > span > label > span.rct-checkbox")
    documents_office_public_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(2) > ol > li:nth-child(1) > span > label > span.rct-checkbox > svg")
    documents_office_private_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(2) > ol > li:nth-child(2) > span > label > span.rct-checkbox > svg")
    documents_office_classified_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(2) > ol > li:nth-child(3) > span > label > span.rct-checkbox > svg")
    documents_office_general_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(2) > ol > li:nth-child(4) > span > label > span.rct-checkbox > svg")
    downloads_check_box = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(3) > span > label > span.rct-checkbox > svg")
    downloads_wordfile_checkbox = (By.CSS_SELECTOR,"#tree-node > ol > li > ol > li:nth-child(3) > ol > li:nth-child(1) > span > label > span.rct-checkbox")
    downloads_excelfile_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(3) > ol > li:nth-child(2) > span > label > span.rct-checkbox")
    home_expand_button = (By.CSS_SELECTOR, "#tree-node > ol > li > span > button")
    desktop_expand_button = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(1) > span > label > span.rct-checkbox > svg")
    documents_expand_button = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > span > button")
    downloads_expand_button = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(3) > span > button")
    check_box_results = (By.CSS_SELECTOR,"div#result")
    
    # Radio Button elements locators
    radio_button_section_button  = (By.CSS_SELECTOR, "div.element-group:nth-of-type(1) #item-2")
    radio_button_section_title = (By.CSS_SELECTOR, "h1.text-center")
    radio_button_yes_button = (By.CSS_SELECTOR, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div:nth-child(3) > div:nth-child(2) > label")
    radio_button_impressive_button = (By.CSS_SELECTOR, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div:nth-child(3) > div:nth-child(3)")
    radio_button_no_option = (By.CSS_SELECTOR, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div:nth-child(3) > div:nth-child(4)")
    radio_button_selection_result = (By.CSS_SELECTOR, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div:nth-child(3) > p > span")
    
    # Web Tables elements locators
    web_tables_section_button  = (By.CSS_SELECTOR, "div.element-group:nth-of-type(1) #item-3")
    web_tables_section_title = (By.CSS_SELECTOR, "h1.text-center")
    web_tables_add_button = (By.ID, "addNewRecordButton")
    web_tables_search_input = (By.CSS_SELECTOR, "div.col input")
    web_tables_search_button = (By.CSS_SELECTOR, "div.col svg")
    web_tables_firstname_header = (By.CSS_SELECTOR, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(1)")
    web_tables_lastname_header = (By.CSS_SELECTOR, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(2)")
    web_tables_age_header = (By.CSS_SELECTOR, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(3)")
    web_tables_email_header = (By.CSS_SELECTOR, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(4)")
    web_tables_salary_header = (By.CSS_SELECTOR, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(5)")
    web_tables_department_header = (By.CSS_SELECTOR, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(6)")
    web_tables_elementone_edit_button = (By.CSS_SELECTOR, "#edit-record-1 > svg")
    web_tables_elementtwo_edit_button = (By.CSS_SELECTOR, "#edit-record-2 > svg")
    web_tables_elementthree_edit_button = (By.CSS_SELECTOR, "#edit-record-3 > svg")
    web_tables_elementfour_edit_button = (By.CSS_SELECTOR, "#edit-record-4 > svg")
    web_tables_elementone_delete_button = (By.CSS_SELECTOR, "#delete-record-1 > svg")
    web_tables_elementtwo_delete_button = (By.CSS_SELECTOR, "#delete-record-2 > svg")
    web_tables_elementthree_delete_button = (By.CSS_SELECTOR, "#delete-record-3 > svg")
    web_tables_elementfour_delete_button = (By.CSS_SELECTOR, "#delete-record-4 > svg")
    web_tables_registration_firstname_field = (By.ID, "firstName")
    web_tables_registration_lastname_field = (By.ID, "lastName")
    web_tables_registration_email_field = (By.ID, "userEmail")
    web_tables_registration_age_field = (By.ID, "age")
    web_tables_registration_salary_field = (By.ID, "salary")
    web_tables_registration_department_field = (By.ID, "department")
    web_tables_registration_submit_button = (By.ID, "submit")
    web_tables_firstname_field = (By.CSS_SELECTOR, "div.rt-tr-group:nth-of-type(1) div.rt-td:nth-of-type(1)")
    web_tables_lastname_field = (By.CSS_SELECTOR, "div.rt-tr-group:nth-of-type(1) div.rt-td:nth-of-type(2)")
    web_tables_age_field = (By.CSS_SELECTOR, "div.rt-tr-group:nth-of-type(1) div.rt-td:nth-of-type(3)")
    web_tables_email_field = (By.CSS_SELECTOR, "div.rt-tr-group:nth-of-type(1) div.rt-td:nth-of-type(4)")
    web_tables_salary_field = (By.CSS_SELECTOR, "div.rt-tr-group:nth-of-type(1) div.rt-td:nth-of-type(5)")
    web_tables_department_field = (By.CSS_SELECTOR, "div.rt-tr-group:nth-of-type(1) div.rt-td:nth-of-type(6)")
    
    # Buttons elements locators
    buttons_section_button  = (By.CSS_SELECTOR, "div.element-group:nth-of-type(1) #item-4")
    buttons_section_title = (By.CSS_SELECTOR, "h1.text-center")
    buttons_double_click_button = (By.ID, "doubleClickBtn")
    buttons_double_click_message = (By.ID, "doubleClickMessage")
    buttons_right_click_button = (By.ID, "rightClickBtn")
    buttons_right_click_message = (By.ID, "rightClickMessage")
    buttons_click_button = (By.CSS_SELECTOR, "div.col-12:nth-of-type(2) div.mt-4:nth-of-type(3) button")
    buttons_click_message = (By.ID, "dynamicClickMessage")
    
    # Links elements locators
    links_section_button  = (By.CSS_SELECTOR, "div.element-group:nth-of-type(1) #item-5")
    links_section_title = (By.CSS_SELECTOR, "h1.text-center")
    links_home_link = (By.ID,"simpleLink")
    links_created_link = (By.ID, "created")
    links_no_content_link = (By.ID, "no-content")
    links_moved_link = (By.ID, "moved")
    links_bad_request_link = (By.ID, "bad-request")
    links_unauthorized_link = (By.ID, "unauthorized")
    links_forbidden_link = (By.ID, "forbidden")
    links_not_found_link = (By.ID, "invalid-url")
    links_results = (By.ID, "linkResponse")
    
    # Upload and Download elements locators
    upload_section_button  = (By.CSS_SELECTOR, "div.element-group:nth-of-type(1) #item-7")
    upload_section_title = (By.CSS_SELECTOR, "h1.text-center")
    upload_button = (By.ID, "uploadFile")
    download_button = (By.ID, "downloadButton")
    upload_uploaded_file_path = ( By.ID, "uploadedFilePath")
    
    # Dynamic Properties elements locators
    dynamic_properties_section_button  = (By.CSS_SELECTOR, "div.element-group:nth-of-type(1) #item-8")
    dynamic_properties_section_title = (By.CSS_SELECTOR, "h1.text-center")
    dynamic_properties_random_id_text = (By.XPATH, "//p[contains(text(), 'This text has random Id')]")
    dynamic_properties_enable_button = (By.ID, "enableAfter")
    dynamic_properties_color_change_button = (By.ID, "colorChange")
    dynamic_properties_visible_after_button = (By.ID, "visibleAfter")
    
    
    def __init__(self, driver):
        super().__init__(driver)
        