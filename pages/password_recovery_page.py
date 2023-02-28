from tests.base_page import PageBase
from tests.base_page import PageBaseLocators
from selenium.webdriver.common.by import By


class RosTelecomLocators_RECOVERY(PageBase, PageBaseLocators):
    LOCATOR_FORGOT_PASS = (By.ID, 'forgot_password')
    LOCATOR_RT_REC_PHONE = (By.ID, "t-btn-tab-phone")
    LOCATOR_RT_REC_MAIL = (By.ID, "t-btn-tab-mail")
    LOCATOR_RT_REC_LOGIN = (By.ID, "t-btn-tab-login")
    LOCATOR_RT_REC_LS = (By.ID, "t-btn-tab-ls")
    LOCATOR_RT_REC_USERNAME = (By.ID, "username")
    LOCATOR_RT_REC_INPUT_CAPTCHA = (By.ID, "captcha")
    LOCATOR_RT_REC_PHONE_TAB_ACTIVE = (By.CSS_SELECTOR, '#t-btn-tab-phone.rt-tab--active')
    LOCATOR_RT_REC_MAIL_TAB_ACTIVE = (By.CSS_SELECTOR, '#t-btn-tab-mail.rt-tab--active')
    LOCATOR_RT_REC_LOGIN_TAB_ACTIVE = (By.CSS_SELECTOR, '#t-btn-tab-login.rt-tab--active')
    LOCATOR_RT_REC_LS_TAB_ACTIVE = (By.CSS_SELECTOR, '#t-btn-tab-ls.rt-tab--active')
    LOCATOR_RT_REC_CONTINUE = (By.CSS_SELECTOR, '#reset')
    LOCATOR_RT_REC_BACK = (By.CSS_SELECTOR, '#reset-back')
    LOCATOR_RT_REC_MESSAGE_ABOUT_PASSWORD_RECOVERY = (By.CLASS_NAME, 'card-container__title')
    LOCATOR_LOGO = (By.CSS_SELECTOR, 'header#app-header > div > div > svg')


    def should_be_message_about_password_recovery(self):
        assert self.is_element_present(*RosTelecomLocators_RECOVERY.LOCATOR_RT_REC_MESSAGE_ABOUT_PASSWORD_RECOVERY)

    def should_be_login_form(self):
        assert self.is_element_present(*RosTelecomLocators_RECOVERY.LOCATOR_RT_REC_USERNAME), "User name form is not presented"

    def should_have_tabs(self):
        assert self.is_element_present(*RosTelecomLocators_RECOVERY.LOCATOR_RT_REC_MAIL)
        assert self.is_element_present(*RosTelecomLocators_RECOVERY.LOCATOR_RT_REC_PHONE)
        assert self.is_element_present(*RosTelecomLocators_RECOVERY.LOCATOR_RT_REC_LOGIN)
        assert self.is_element_present(*RosTelecomLocators_RECOVERY.LOCATOR_RT_REC_LS)

    def should_have_active_telephone_tab(self):
        assert self.is_element_present(*RosTelecomLocators_RECOVERY.LOCATOR_RT_REC_PHONE_TAB_ACTIVE), "TELEPHONE TAB is not active"

    def should_have_active_email_tab(self):
        assert self.is_element_present(*RosTelecomLocators_RECOVERY.LOCATOR_RT_REC_MAIL_TAB_ACTIVE), "EMAIL TAB is not active"

    def should_have_active_login_tab(self):
        assert self.is_element_present(*RosTelecomLocators_RECOVERY.LOCATOR_RT_REC_LOGIN_TAB_ACTIVE), "LOGIN TAB is not active"

    def should_have_active_account_tab(self):
        assert self.is_element_present(*RosTelecomLocators_RECOVERY.LOCATOR_RT_REC_LS_TAB_ACTIVE), "ACCOUNT TAB is not active"

    def should_have_logo(self):
        assert self.is_element_present(*RosTelecomLocators_RECOVERY.LOCATOR_LOGO), "LOGO is not presented"

    def should_have_captcha(self):
        self.is_element_present(*RosTelecomLocators_RECOVERY.LOCATOR_RT_REC_INPUT_CAPTCHA)

    def click_forgot_pass_button(self):
        assert self.is_element_present(*RosTelecomLocators_RECOVERY.LOCATOR_FORGOT_PASS)



