from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AlertsPage(BasePage):
    
    # Browser Windows elements locators
    browser_windows_section_button = (By.CSS_SELECTOR, "div.left-pannel div.element-group:nth-of-type(3) div.element-list ul #item-0")
    browser_windows_section_title = (By.CSS_SELECTOR, "h1.text-center")
    browser_windows_new_tab_button = (By.ID, "tabButton")
    browser_windows_new_window_button = (By.ID, "windowButton")
    browser_windows_new_window_message_button = (By.ID, "messageWindowButton")
    browser_windows_message_content = (By.CSS_SELECTOR, "body")
    
    # Alerts elements locators
    alerts_section_button = (By.CSS_SELECTOR, "div.left-pannel div.element-group:nth-of-type(3) div.element-list ul #item-1")
    alerts_section_title = (By.CSS_SELECTOR, "h1.text-center")
    alert_instant_alert_button = (By.ID, "alertButton")
    alert_five_seconds_alert_button = (By.ID,"timerAlertButton")
    alert_confirm_box_button = (By.ID, "confirmButton")
    alert_confirm_button_message = (By.ID, "confirmResult")
    alert_prompt_button = (By.ID, "promtButton")
    alert_prompt_result = (By.ID, "promptResult")
    
    # Frames elements locators
    frames_section_button = (By.CSS_SELECTOR, "div.left-pannel div.element-group:nth-of-type(3) div.element-list ul #item-2")
    frames_section_title = (By.CSS_SELECTOR, "h1.text-center")
    frames_frame_1 = (By.ID, "frame1")
    frames_fame_1_header = (By.ID, "sampleHeading")
    frames_frame_2 = (By.ID, "frame2")
    frames_fame_2_header = (By.ID, "sampleHeading")
    
    # Nested frames elements
    nested_frames_section_button = (By.CSS_SELECTOR, "div.left-pannel div.element-group:nth-of-type(3) div.element-list ul #item-3")
    nested_frames_section_title = (By.CSS_SELECTOR, "h1.text-center")
    nested_frames_parent_frame = (By.ID, "frame1")
    nested_frames_parent_frame_content = (By.CSS_SELECTOR, "#frame1 body")
    nested_frames_child_frame = (By.XPATH, "//iframe[@srcdoc='<p>Child Iframe</p>']")
    
    # Modal Dialogs elements
    modal_dialogs_section_button = (By.CSS_SELECTOR, "div.left-pannel div.element-group:nth-of-type(3) div.element-list ul #item-4")
    modal_dialogs_section_title = (By.CSS_SELECTOR, "h1.text-center")
    modal_dialogs_small_modal_button = (By.ID, "showSmallModal")
    modal_dialogs_small_modal_content = (By.CSS_SELECTOR, "body > div.fade.modal.show > div > div > div.modal-body")
    modal_dialogs_small_modal_close_button = (By.ID, "closeSmallModal")
    modal_dialogs_large_modal_button = (By.ID, "showLargeModal")
    modal_dialogs_large_modal_modal_content = (By.CSS_SELECTOR, "body > div.fade.modal.show > div > div > div.modal-body")
    modal_dialogs_large_modal_close_button = (By.ID, "closeLargeModal")
    
    
    
    
    def __init__(self, driver):
        super().__init__(driver)