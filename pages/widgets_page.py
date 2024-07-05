from datetime import datetime, timedelta

from selenium.webdriver import ActionChains
from pages import base_page
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class WidgetsPage(BasePage):
    
    # Accordian elements locators.
    widgets_accordian_section_button = (By.CSS_SELECTOR, "div.left-pannel div.element-group:nth-of-type(4) div.element-list ul #item-0")
    widgets_section_title = (By.CSS_SELECTOR, "h1.text-center")
    widgets_accordian_header_section_1 = (By.ID, "section1Heading")
    widgets_accordian_content_section_1 = (By.ID, "section1Content")
    widgets_accordian_header_section_2 = (By.ID, "section2Heading")
    widgets_accordian_content_section_2 = (By.ID, "section2Content")
    widgets_accordian_header_section_3 = (By.ID, "section3Heading")
    widgets_accordian_content_section_3 = (By.ID, "section3Content")
    
    # Auto Complete elements locators
    widgets_autocomplete_section_button = (By.CSS_SELECTOR, "div.left-pannel div.element-group:nth-of-type(4) div.element-list ul #item-1")
    widgets_autocomplete_section_title = (By.CSS_SELECTOR, "h1.text-center")
    widgets_autocomplete_multiple_field = (By.CSS_SELECTOR, "#autoCompleteMultipleContainer input")
    widgets_autocomplete_multiple_tag_1 = (By.CSS_SELECTOR, "#autoCompleteMultipleContainer div.auto-complete__multi-value div:nth-of-type(1)")
    widgets_autocomplete_multiple_tag_2 = (By.CSS_SELECTOR, "#autoCompleteMultipleContainer > div > div.auto-complete__value-container > div:nth-child(2) > div.auto-complete__multi-value__label")
    widgets_autocomplete_single_field = (By.ID, "autoCompleteSingleContainer")
    widgets_autocomplete_single_field_value = (By.CSS_SELECTOR, "#autoCompleteSingleContainer div.auto-complete__single-value")

    # Date Picker elements locators
    widgets_date_picker_section_button = (By.CSS_SELECTOR, "div.left-pannel div.element-group:nth-of-type(4) div.element-list ul #item-2")
    widgets_date_picker_section_title = (By.CSS_SELECTOR, "h1.text-center")
    widgets_date_picker_date_selector = (By.ID, "datePickerMonthYearInput")
    widgets_date_picker_date_selector_field = (By.CSS_SELECTOR, "div#datePickerMonthYear div.react-datepicker__input-container input")
    widgets_date_picker_date_selector_month = (By.CSS_SELECTOR, "select.react-datepicker__month-select")
    widgets_date_picker_date_selector_august = (By.CSS_SELECTOR, "#datePickerMonthYear > div.react-datepicker__tab-loop > div.react-datepicker-popper > div > div > div.react-datepicker__month-container > div.react-datepicker__header > div.react-datepicker__header__dropdown.react-datepicker__header__dropdown--select > div.react-datepicker__month-dropdown-container.react-datepicker__month-dropdown-container--select > select > option:nth-child(8)")
    widgets_date_picker_date_selector_year = (By.CSS_SELECTOR, "select.react-datepicker__year-select")
    widgets_date_picker_date_selector_1989 = (By.CSS_SELECTOR, "#datePickerMonthYear > div.react-datepicker__tab-loop > div.react-datepicker-popper > div > div > div.react-datepicker__month-container > div.react-datepicker__header > div.react-datepicker__header__dropdown.react-datepicker__header__dropdown--select > div.react-datepicker__year-dropdown-container.react-datepicker__year-dropdown-container--select > select > option:nth-child(90)")
    widgets_date_picker_date_selector_day_28 = (By.CSS_SELECTOR, "#datePickerMonthYear > div.react-datepicker__tab-loop > div.react-datepicker-popper > div > div > div.react-datepicker__month-container > div.react-datepicker__month > div:nth-child(5) > div.react-datepicker__day.react-datepicker__day--028")
    widgets_date_picker_date_time_selector = (By.ID, "dateAndTimePickerInput")
    widgets_date_picker_date_time_selector_field = (By.ID, "dateAndTimePickerInput")
    widgets_date_picker_date_time_month = (By.CSS_SELECTOR, "span.react-datepicker__month-read-view--selected-month")
    widgets_date_picker_date_time_august = (By.CSS_SELECTOR, "#dateAndTimePicker > div.react-datepicker__tab-loop > div.react-datepicker-popper > div > div > div.react-datepicker__month-container > div.react-datepicker__header > div.react-datepicker__header__dropdown.react-datepicker__header__dropdown--scroll > div.react-datepicker__month-dropdown-container.react-datepicker__month-dropdown-container--scroll > div.react-datepicker__month-dropdown > div:nth-child(8)")
    widgets_date_picker_date_time_year = (By.CSS_SELECTOR, "span.react-datepicker__year-read-view--selected-year")
    widgets_date_picker_date_time_2024 = (By.CSS_SELECTOR, "#dateAndTimePicker > div.react-datepicker__tab-loop > div.react-datepicker-popper > div > div > div.react-datepicker__month-container > div.react-datepicker__header > div.react-datepicker__header__dropdown.react-datepicker__header__dropdown--scroll > div.react-datepicker__year-dropdown-container.react-datepicker__year-dropdown-container--scroll > div.react-datepicker__year-dropdown > div.react-datepicker__year-option.react-datepicker__year-option--selected_year")
    widgets_date_picker_date_time_day_28 = (By.CSS_SELECTOR, "#dateAndTimePicker > div.react-datepicker__tab-loop > div.react-datepicker-popper > div > div > div.react-datepicker__month-container > div.react-datepicker__month > div:nth-child(5) > div.react-datepicker__day.react-datepicker__day--028")
    widgets_date_picker_date_time_current = (By.CSS_SELECTOR, "#dateAndTimePicker > div.react-datepicker__tab-loop > div.react-datepicker-popper > div > div > div.react-datepicker__time-container > div.react-datepicker__time > div > ul > li.react-datepicker__time-list-item.react-datepicker__time-list-item--selected")

    # Date Picker functions
    def round_time_to_nearest_quarter_hour(self):
        current_time = datetime.now()
        # Redondea el tiempo al cuarto de hora más cercano
        rounded_minute = ((current_time.minute + 7) // 15) * 15
        # Ajusta las horas si es necesario
        if rounded_minute >= 60:
            current_time += timedelta(hours=1)
            rounded_minute = 0
        # Crea un nuevo objeto datetime con el tiempo redondeado
        rounded_time = current_time.replace(minute=rounded_minute, second=0, microsecond=0)
        return rounded_time.strftime("%I:%M %p")
    
    def calculate_time_selector_index(self, rounded_time_str):
        # Convert the rounded time string to a datetime object
        rounded_time = datetime.strptime(rounded_time_str, "%I:%M %p")
        # Calculate the index based on the 24-hour format hour and minutes
        index = rounded_time.hour * 4 + rounded_time.minute // 15 + 1
        # Return the index
        return index
    
    
    # Slider elements locators
    widgets_slider_section_button = (By.CSS_SELECTOR, "div.left-pannel div.element-group:nth-of-type(4) div.element-list ul #item-3")
    widgets_slider_section_title = (By.CSS_SELECTOR, "h1.text-center")
    widgets_slider_button = (By.CSS_SELECTOR, "div#sliderContainer input")
    widgets_slider_value = (By.ID, "sliderValue")
    
    # Slider functions
    def move_slider(self, slider_locator, value):
        """Moves the slider to the specified value (between 0 and 100)."""
        slider_element = self.driver.find_element(*slider_locator)
        #ActionChains(self).drag_and_drop_by_offset(slider_element, value, 0).perform()
        ActionChains(self).click_and_hold(slider_element).pause(1).move_by_offset(50, 0).release().perform()
    
    
    # Progress Bar elements locators
    widgets_progress_bar_section_button = (By.CSS_SELECTOR, "div.left-pannel div.element-group:nth-of-type(4) div.element-list ul #item-4")
    widgets_progress_bar_section_title = (By.CSS_SELECTOR, "h1.text-center")
    widgets_progress_bar_start_button = (By.ID, "startStopButton")
    widgets_progress_bar_bar = (By.CSS_SELECTOR, "#progressBar div.progress-bar")
    widgets_progress_bar_restart_button = (By.ID, "resetButton")
    
    # Tabs elements locators
    widgets_tabs_section_button = (By.CSS_SELECTOR, "div.left-pannel div.element-group:nth-of-type(4) div.element-list ul #item-5")
    widgets_tabs_section_title = (By.CSS_SELECTOR, "h1.text-center")
    widgets_tabs_what_tab = (By.ID, "demo-tab-what")
    widgets_tabs_what_tab_content = (By.ID ,"demo-tabpane-what")
    widgets_tabs_origin_tab = (By.ID, "demo-tab-origin")
    widgets_tabs_origin_tab_content = (By.ID, "demo-tabpane-origin")
    widgets_tabs_use_tab = (By.ID, "demo-tab-use")
    widgets_tabs_use_tab_content = (By.ID, "demo-tabpane-use")
    
    # Tool Tips elements locators
    widgets_tooltips_section_button = (By.CSS_SELECTOR, "div.left-pannel div.element-group:nth-of-type(4) div.element-list ul #item-6")
    widgets_tooltips_section_title = (By.CSS_SELECTOR, "h1.text-center")
    widgets_tooltips_hover_button = (By.ID, "toolTipButton")
    widgets_tooltips_hover_field = (By.ID, "toolTipTextField")
    widgets_tooltips_word = (By.CSS_SELECTOR, "#texToolTopContainer > a:nth-child(1)")
    widgets_tooltips_numbers = (By.CSS_SELECTOR, "#texToolTopContainer > a:nth-child(2)")
    
    # Menu elements locators
    widgets_menu_section_button = (By.CSS_SELECTOR, "div.left-pannel div.element-group:nth-of-type(4) div.element-list ul #item-7")
    widgets_menu_section_title = (By.CSS_SELECTOR, "h1.text-center")
    widgets_menu_menu_item_1 = (By.CSS_SELECTOR, "#nav > li:nth-child(1)")
    widgets_menu_menu_item_2 = (By.CSS_SELECTOR, "#nav > li:nth-child(2)")
    widgets_menu_menu_item_3 = (By.CSS_SELECTOR, "#nav > li:nth-child(3)")
    widgets_menu_menu_sub_item_1 = (By.CSS_SELECTOR, "#nav > li:nth-child(2) > ul > li:nth-child(1) > a")
    widgets_menu_menu_sub_item_2 = (By.CSS_SELECTOR, "#nav > li:nth-child(2) > ul > li:nth-child(2) > a")
    widgets_menu_menu_sub_sub_list = (By.CSS_SELECTOR, "#nav > li:nth-child(2) > ul > li:nth-child(3) > a")
    widgets_menu_sub_sub_item_1 = (By.CSS_SELECTOR, "#nav > li:nth-child(2) > ul > li:nth-child(3) > ul > li:nth-child(1) > a")
    widgets_menu_sub_sub_item_2 = (By.CSS_SELECTOR, "#nav > li:nth-child(2) > ul > li:nth-child(3) > ul > li:nth-child(2) > a")
    
    # Select Menu elements locators
    widgets_select_menu_section_button = (By.CSS_SELECTOR, "div.left-pannel div.element-group:nth-of-type(4) div.element-list ul #item-8")
    widgets_select_menu_section_title = (By.CSS_SELECTOR, "h1.text-center")
    widgets_select_menu_select_value = (By.CSS_SELECTOR, "div#withOptGroup div div div input")
    widgets_select_menu_value_result = (By.CSS_SELECTOR, "div#withOptGroup div div div")
    widgets_select_menu_select_one = (By.CSS_SELECTOR, "div#selectOne div div div input")
    widgets_select_menu_select_one_result = (By.CSS_SELECTOR, "div#selectOne div div div")
    widgets_select_menu_old_style = (By.ID, "oldSelectMenu")
    widgets_select_menu_old_style_black = (By.CSS_SELECTOR, "#oldSelectMenu > option:nth-child(6)")
    

    def __init__(self, driver):
        super().__init__(driver)