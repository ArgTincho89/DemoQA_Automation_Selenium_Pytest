
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.home_page import HomePage
from pages.widgets_page import WidgetsPage
from tests.base_test import BaseTest




class TestWidgets(BaseTest):
    
    def test_01_accordian(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Widgets
        widgets_link = home_page.find(*home_page.Widgets)
        self.driver.execute_script("arguments[0].click();", widgets_link)
        # Creation of an Widgets Page instance
        widgets_page = WidgetsPage(self.driver)
        # Navigate to Accordian section
        widgets_page.click(*widgets_page.widgets_accordian_section_button)
        # Asserting that the tittle of the section corresponds to Accordian
        widgets_page.assert_text(widgets_page.widgets_section_title, "Accordian")
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        time.sleep(0.5)
        # Clicking the first header and asserting the content
        widgets_page.click(*widgets_page.widgets_accordian_header_section_1)
        time.sleep(0.1)
        widgets_page.assert_content_contains(widgets_page.widgets_accordian_content_section_1, "Lorem Ipsum")
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        time.sleep(0.5)
        # Clicking the second header and asserting the content
        widgets_page.click(*widgets_page.widgets_accordian_header_section_2)
        time.sleep(0.1)
        widgets_page.assert_content_contains(widgets_page.widgets_accordian_content_section_2, "Contrary to popular belief")
        # Clicking the third header and asserting the content
        widgets_page.click(*widgets_page.widgets_accordian_header_section_3)
        time.sleep(0.1)
        widgets_page.assert_content_contains(widgets_page.widgets_accordian_content_section_3, "It is a long established fact")
    
    def test_02_auto_complete(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Widgets page
        widgets_link = home_page.find(*home_page.Widgets)
        self.driver.execute_script("arguments[0].click();", widgets_link)
        # Creation of an Widgets Page instance
        widgets_page = WidgetsPage(self.driver)
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        time.sleep(0.5)
        # Navigate to Auto Complete section
        widgets_page.click(*widgets_page.widgets_autocomplete_section_button)
        # Asserting that the tittle of the section corresponds to Auto Complete
        widgets_page.assert_text(widgets_page.widgets_autocomplete_section_title, "Auto Complete")
        # Clicking the multiple color names field
        widgets_page.click(*widgets_page.widgets_autocomplete_multiple_field)
        # Inputing a value using the auto complete function
        widgets_page.set_multiple(widgets_page.widgets_autocomplete_multiple_field, "b", "DOWN", "ENTER")
        # Asserting that the value "Black" is correctly displayed in the first tag
        time.sleep(0.5)
        widgets_page.assert_text(widgets_page.widgets_autocomplete_multiple_tag_1, "Black")
        # Inputting a second value using the auto complete function
        widgets_page.set_multiple(widgets_page.widgets_autocomplete_multiple_field, "y", "RIGHT", "ENTER", clear=False)
        # Asserting that the value "Yellow" is correctly displayed in the second tag
        time.sleep(0.5)
        widgets_page.assert_text(widgets_page.widgets_autocomplete_multiple_tag_2, "Yellow")
        
    def test_03_date_picker(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Widgets page
        widgets_link = home_page.find(*home_page.Widgets)
        self.driver.execute_script("arguments[0].click();", widgets_link)
        # Creation of an Widgets Page instance
        widgets_page = WidgetsPage(self.driver)
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        time.sleep(0.5)
        # Navigate to Date Picker section
        widgets_page.click(*widgets_page.widgets_date_picker_section_button)
        # Asserting that the tittle of the section corresponds to Date Picker
        widgets_page.assert_text(widgets_page.widgets_date_picker_section_title, "Date Picker")
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        time.sleep(0.5)
        # Opening the "Select Date" picker and inputing the date August 28th, 1989
        widgets_page.click(*widgets_page.widgets_date_picker_date_selector)
        widgets_page.click(*widgets_page.widgets_date_picker_date_selector_month)
        widgets_page.click(*widgets_page.widgets_date_picker_date_selector_august)
        widgets_page.click(*widgets_page.widgets_date_picker_date_selector_year)
        widgets_page.click(*widgets_page.widgets_date_picker_date_selector_1989)
        widgets_page.click(*widgets_page.widgets_date_picker_date_selector_day_28)
        # Asserting that the date was correctly selected
        widgets_page.assert_value(widgets_page.widgets_date_picker_date_selector_field, "08/28/1989")
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        time.sleep(0.5)
        # Opening the "Date and Time" picker and inputing the date August 28th, 2024 with the current time.
        widgets_page.click(*widgets_page.widgets_date_picker_date_time_selector)
        widgets_page.click(*widgets_page.widgets_date_picker_date_time_month)
        widgets_page.click(*widgets_page.widgets_date_picker_date_time_august)
        widgets_page.click(*widgets_page.widgets_date_picker_date_time_year)
        widgets_page.click(*widgets_page.widgets_date_picker_date_time_2024)
        widgets_page.click(*widgets_page.widgets_date_picker_date_time_day_28)
        # Rounding and calculating time selector index
        rounded_time_str = widgets_page.round_time_to_nearest_quarter_hour()
        selector_index = widgets_page.calculate_time_selector_index(rounded_time_str)
        # Build the CSS selector using the verified or inspected selector
        css_selector = f"#dateAndTimePicker > div.react-datepicker__tab-loop > div.react-datepicker-popper > div > div > div.react-datepicker__time-container > div.react-datepicker__time > div > ul > li:nth-child({selector_index})"
        # Handle dynamic element if necessary
        wait = WebDriverWait(self.driver, 1)
        time_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
        time_element.click()
        # Asserting that the date was correctly selected
        content = widgets_page.find(*widgets_page.widgets_date_picker_date_time_selector_field)
        content_value = content.get_attribute("value")
        print(f" content value is : {content_value}")
        widgets_page.assert_value_contains(widgets_page.widgets_date_picker_date_time_selector_field, f"August 28, 2024 {rounded_time_str.lstrip('0')}" )
        
    def test_04_slider(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Widgets page
        widgets_link = home_page.find(*home_page.Widgets)
        self.driver.execute_script("arguments[0].click();", widgets_link)
        # Creation of an Widgets Page instance
        widgets_page = WidgetsPage(self.driver)
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        time.sleep(0.5)
        # Navigate to Slider section
        widgets_page.click(*widgets_page.widgets_slider_section_button)
        # Asserting that the tittle of the section corresponds to Slider
        widgets_page.assert_text(widgets_page.widgets_slider_section_title, "Slider")
        # scrolls down 15% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.15);")
        time.sleep(0.5)
        # Define the locator for the slider button
        widgets_slider_button_locator = (By.CSS_SELECTOR, "div#sliderContainer input")
        # Moving the Slider to the right and asserting the correct result
        widgets_slider_button = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(widgets_slider_button_locator))
        actions = ActionChains(self.driver)
        actions.click_and_hold(widgets_slider_button).pause(1).move_by_offset(50, 0).release().perform()
        time.sleep(2)
        widgets_page.assert_value(widgets_page.widgets_slider_value, "60")
        # Moving the Slider to the left and asserting the correct result
        actions.click_and_hold(widgets_slider_button).pause(1).move_by_offset(-100, 0).release().perform()
        time.sleep(2)
        widgets_page.assert_value(widgets_page.widgets_slider_value, "30")
        
    def test_05_progress_bar(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Widgets page
        widgets_link = home_page.find(*home_page.Widgets)
        self.driver.execute_script("arguments[0].click();", widgets_link)
        # Creation of an Widgets Page instance
        widgets_page = WidgetsPage(self.driver)
        # scrolls down 20% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        time.sleep(0.5)
        # Navigate to Progress Bar section
        widgets_page.click(*widgets_page.widgets_progress_bar_section_button)
        # Asserting that the tittle of the section corresponds to Progress Bar
        widgets_page.assert_text(widgets_page.widgets_progress_bar_section_title, "Progress Bar")
        # scrolls down 15% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.15);")
        time.sleep(0.5)
         # Locate progress bar elements
        start_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(widgets_page.widgets_progress_bar_start_button))
        progress_bar = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(widgets_page.widgets_progress_bar_bar))
        # Click the Start button to initiate progress
        start_button.click()
        # Wait for progress bar to reach 50% 
        expected_value = "50"
        while True:
            current_value = progress_bar.get_attribute("aria-valuenow")
            if current_value == expected_value:
                start_button.click()
                break
        time.sleep(1) 
        # Assert that the progress bar value is "50%"
        assert progress_bar.get_attribute("aria-valuenow") == expected_value
        # Resuming the Progress Bar and stopping it when it reaches 75%
        start_button.click()
        expected_value = "75"
        while True:
            current_value = progress_bar.get_attribute("aria-valuenow")
            if current_value == expected_value:
                start_button.click()
                break
        time.sleep(1) 
        # Assert that the progress bar value is "75%"
        assert progress_bar.get_attribute("aria-valuenow") == expected_value
        # Resuming the Progress Bar until it reaches 100%, then restarting and stoping it when it reaches 25%
        start_button.click()
        expected_value = "100"
        while True:
            current_value = progress_bar.get_attribute("aria-valuenow")
            if current_value == expected_value:
                break
        time.sleep(1)
        widgets_page.click(*widgets_page.widgets_progress_bar_restart_button)
        start_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(widgets_page.widgets_progress_bar_start_button))
        start_button.click()
        expected_value = "25"
        while True:
            current_value = progress_bar.get_attribute("aria-valuenow")
            if current_value == expected_value:
                start_button.click()
                break
        
    def test_06_tabs(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Widgets page
        widgets_link = home_page.find(*home_page.Widgets)
        self.driver.execute_script("arguments[0].click();", widgets_link)
        # Creation of an Widgets Page instance
        widgets_page = WidgetsPage(self.driver)
        # scrolls down 30% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.3);")
        time.sleep(0.5)
        # Navigate to tabs section
        widgets_page.click(*widgets_page.widgets_tabs_section_button)
        # Asserting that the tittle of the section corresponds to Tabs
        widgets_page.assert_text(widgets_page.widgets_tabs_section_title, "Tabs")
        # scrolls down 10% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.10);")
        time.sleep(0.5)
        # Clicking the What tab and asserting it's content
        widgets_page.click(*widgets_page.widgets_tabs_what_tab)
        widgets_page.assert_content_contains(widgets_page.widgets_tabs_what_tab_content, "Lorem Ipsum is simply dummy text")
        # Clicking the Origin tab and asserting it's content
        widgets_page.click(*widgets_page.widgets_tabs_origin_tab)
        widgets_page.assert_content_contains(widgets_page.widgets_tabs_origin_tab_content, "Contrary to popular belief")
        # Clicking the Use tab and asserting it's content
        widgets_page.click(*widgets_page.widgets_tabs_use_tab)
        widgets_page.assert_content_contains(widgets_page.widgets_tabs_use_tab_content, "It is a long established fact")
        
    def test_07_tooltips(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Widgets page
        widgets_link = home_page.find(*home_page.Widgets)
        self.driver.execute_script("arguments[0].click();", widgets_link)
        # Creation of an Widgets Page instance
        widgets_page = WidgetsPage(self.driver)
        # scrolls down 30% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.3);")
        time.sleep(0.5)
        # Navigate to Tool Tips section
        widgets_page.click(*widgets_page.widgets_tooltips_section_button)
        # Asserting that the tittle of the section corresponds to Tool Tips
        widgets_page.assert_text(widgets_page.widgets_tooltips_section_title, "Tool Tips")
        # scrolls down 10% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.10);")
        time.sleep(0.5)
        # Preparing the elements
        hover_button = widgets_page.find(*widgets_page.widgets_tooltips_hover_button)
        hover_field = widgets_page.find(*widgets_page.widgets_tooltips_hover_field)
        hover_word = widgets_page.find(*widgets_page.widgets_tooltips_word)
        hover_numbers = widgets_page.find(*widgets_page.widgets_tooltips_numbers)
        # Hovering over the "Hover me to see" button and asserting the appearence of the corresponding tooltip.
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_button).perform()
        WebDriverWait(self.driver, 10).until(
            lambda _: hover_button.get_attribute("aria-describedby"))
        assert hover_button.get_attribute("aria-describedby") == "buttonToolTip"
        # Hovering over the "Homer me to see" field and asserting the appearence of the corresponding tooltip.
        actions.move_to_element(hover_field).perform()
        WebDriverWait(self.driver, 10).until(
            lambda _: hover_field.get_attribute("aria-describedby"))
        assert hover_field.get_attribute("aria-describedby") == "textFieldToolTip"
        # Hovering over the "Contrary" word and asserting the appearence of the corresponding tooltip.
        actions.move_to_element(hover_word).perform()
        WebDriverWait(self.driver, 10).until(
            lambda _: hover_word.get_attribute("aria-describedby"))
        assert hover_word.get_attribute("aria-describedby") == "contraryTexToolTip"
        # Hovering over the "numbers" and asserting the appearence of the corresponding tooltip.
        actions.move_to_element(hover_numbers).perform()
        WebDriverWait(self.driver, 10).until(
            lambda _: hover_numbers.get_attribute("aria-describedby"))
        assert hover_numbers.get_attribute("aria-describedby") == "sectionToolTip"
        
    def test_08_menu(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Widgets page
        widgets_link = home_page.find(*home_page.Widgets)
        self.driver.execute_script("arguments[0].click();", widgets_link)
        # Creation of an Widgets Page instance
        widgets_page = WidgetsPage(self.driver)
        # scrolls down 50% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.5);")
        time.sleep(0.5)
        # Navigate to Menu section
        widgets_page.click(*widgets_page.widgets_menu_section_button)
        # Asserting that the tittle of the section corresponds to Menu
        widgets_page.assert_text(widgets_page.widgets_menu_section_title, "Menu")
        # scrolls to the Menu title and scrolls down 10%
        menu_title = self.driver.find_element(*widgets_page.widgets_menu_section_title)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", menu_title)
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.1);")
        time.sleep(1)
        # Asserting the "Main Item 1" menu option is present
        widgets_page.find(*widgets_page.widgets_menu_menu_item_1)
        # Hovering over "Main Item 2"
        main_item_2 = widgets_page.find(*widgets_page.widgets_menu_menu_item_2)
        actions = ActionChains(self.driver)
        actions.move_to_element(main_item_2).perform()
        # Hovering over "sub item 1"
        sub_item_1 = widgets_page.find(*widgets_page.widgets_menu_menu_sub_item_1)
        actions.move_to_element(sub_item_1).perform()
        # Hovering over "sub item 2"
        sub_item_2 = widgets_page.find(*widgets_page.widgets_menu_menu_sub_item_2)
        actions.move_to_element(sub_item_2).perform()
        # Hovering over "SUB SUB LIST"
        sub_sub_list = widgets_page.find(*widgets_page.widgets_menu_menu_sub_sub_list)
        actions.move_to_element(sub_sub_list).perform()
        # Hovering over "sub sub item 1"
        sub_sub_item_1 = widgets_page.find(*widgets_page.widgets_menu_sub_sub_item_1)
        actions.move_to_element(sub_sub_item_1).perform()
        # Hovering over "sub sub item 2"
        sub_sub_item_2 = widgets_page.find(*widgets_page.widgets_menu_sub_sub_item_2)
        actions.move_to_element(sub_sub_item_2).perform()
        # Hovering over "Main Item 3"
        main_item_3 = widgets_page.find(*widgets_page.widgets_menu_menu_item_3)
        actions.move_to_element(main_item_3).perform() 
        
    def test_09_select_menu(self):
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to Widgets page
        widgets_link = home_page.find(*home_page.Widgets)
        self.driver.execute_script("arguments[0].click();", widgets_link)
        # Creation of an Widgets Page instance
        widgets_page = WidgetsPage(self.driver)
        # scrolls down 50% to enable better elements visibility
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.5);")
        time.sleep(0.5)
        # Navigate to Select Menu section
        widgets_page.click(*widgets_page.widgets_select_menu_section_button)
        # Asserting that the tittle of the section corresponds to Menu
        widgets_page.assert_text(widgets_page.widgets_menu_section_title, "Select Menu")
        # scrolls to the Select Menu title and scrolls down 10%
        select_menu_title = widgets_page.find(*widgets_page.widgets_select_menu_section_title)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", select_menu_title)
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.2);")
        time.sleep(1)
        # Selecting an option in the "Select Value" selector
        select_value = widgets_page.find(*widgets_page.widgets_select_menu_select_value)
        self.driver.execute_script("arguments[0].click();", select_value)
        widgets_page.set_multiple(widgets_page.widgets_select_menu_select_value, "DOWN", "DOWN", "DOWN", "ENTER", clear=False)
        # Asserting the correct value is set
        widgets_page.assert_text(widgets_page.widgets_select_menu_value_result, "Group 2, option 1")
        # Selection an opton in the "Select One" selector
        select_one = widgets_page.find(*widgets_page.widgets_select_menu_select_one)
        self.driver.execute_script("arguments[0].click();", select_one)
        time.sleep(1)
        widgets_page.set_multiple(widgets_page.widgets_select_menu_select_one, "DOWN", "ENTER", clear=False)
        # Asserting the correct value is set
        widgets_page.assert_text(widgets_page.widgets_select_menu_select_one_result, "Dr.")
        # Selecting an option in the "Old Style" select menu
        old_style = widgets_page.find(*widgets_page.widgets_select_menu_old_style)
        self.driver.execute_script("arguments[0].click();", old_style)
        time.sleep(3)
        #widgets_page.set_multiple(widgets_page.widgets_select_menu_select_value, "DOWN", "DOWN", "DOWN", "DOWN", "DOWN", "ENTER", clear=False)
        # Asserting the correct option was selected
        old_style_element = widgets_page.find(*widgets_page.widgets_select_menu_old_style)
        element_text = old_style_element.text
        options_list = element_text.split("\n")
        first_option = options_list[0]
        print(f"element text is {first_option}")
        #widgets_page.assert_value(widgets_page.widgets_select_menu_old_style, "Red")
        widgets_page.assert_text(*first_option, "Red")
        