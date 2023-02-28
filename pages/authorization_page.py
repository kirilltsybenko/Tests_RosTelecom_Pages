from tests.base_page import PageBase
from tests.base_page import PageBaseLocators
from selenium.webdriver.common.by import By


class RosTelecomLocators_LOGIN(PageBase, PageBaseLocators):
    LOCATOR_RT_AUTH_BY_PHONE = (By.ID, "t-btn-tab-phone")
    LOCATOR_RT_AUTH_BY_MAIL = (By.ID, "t-btn-tab-mail")
    LOCATOR_RT_AUTH_BY_LOGIN = (By.ID, "t-btn-tab-login")
    LOCATOR_RT_AUTH_BY_LS = (By.ID, "t-btn-tab-ls")
    LOCATOR_RT_REMEMBER_ME = (By.CSS_SELECTOR, "rt-checkbox__label")
    LOCATOR_RT_FORGOT_PASS = (By.ID, "forgot_password")
    LOCATOR_RT_LOGO = (By.CSS_SELECTOR, '.rt-logo.what-is-container__logo')
    LOCATOR_RT_AUTH_BY_PHONE_ACTIVE = (By.CLASS_NAME, 'rt-tab rt-tab--small rt-tab--active')
    LOCATOR_RT_AUTH_BY_MAIL_ACTIVE = (By.CSS_SELECTOR, '#t-btn-tab-mail.rt-tab--active')
    LOCATOR_RT_AUTH_BY_LOGIN_ACTIVE = (By.CSS_SELECTOR, '#t-btn-tab-login.rt-tab--active')
    LOCATOR_RT_AUTH_BY_LS_ACTIVE = (By.CSS_SELECTOR, '#t-btn-tab-ls.rt-tab--active')
    LOGIN_LOCATOR = (By.CSS_SELECTOR, "#login_form")
    LOCATOR_ERROR_MESSAGE = (By.ID, 'form-error-message')
    REGISTER_LOCATOR = (By.ID, "kc-register")
    USERNAME_LOCATOR = (By.ID, 'username')
    PASSWORD_LOCATOR = (By.ID, 'password')
    ENTER_BUTTON_LOCATOR = (By.ID, 'kc-login')
    LOGOUT_BUTTON_LOCATOR = (By.ID, 'logout-btn')
    ACCOUNT_ICON_LOCATOR = (By.CSS_SELECTOR, '.sc-bvFjSx.iqOiiv')
    EXIT_LOCATOR = (By.ID, 'logout-btn')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOCATOR_FORGOT_PASS = (By.ID, 'forgot_password')



    def open(self):
        self.browser.get(self.url)

    def authorization_by_phone(self):
        self.find_element(RosTelecomLocators_LOGIN.LOCATOR_RT_AUTH_BY_PHONE, time=3).click()

    def authorizations_by_mail(self):
        self.find_element(RosTelecomLocators_LOGIN.LOCATOR_RT_AUTH_BY_MAIL, time=3).click()

    def authorizations_by_login(self):
        self.find_element(RosTelecomLocators_LOGIN.LOCATOR_RT_AUTH_BY_LOGIN, time=3).click()

    def authorizations_by_ls(self):
        self.find_element(RosTelecomLocators_LOGIN.LOCATOR_RT_AUTH_BY_LS, time=3).click()

    def if_there_is_logo(self):
        self.find_element(RosTelecomLocators_LOGIN.LOCATOR_RT_LOGO, time=3)

    def should_have_active_phone_tab(self):
        self.is_element_present(*RosTelecomLocators_LOGIN.LOCATOR_RT_AUTH_BY_PHONE_ACTIVE)

    def should_have_active_email_tab(self):
        assert self.is_element_present(*RosTelecomLocators_LOGIN.LOCATOR_RT_AUTH_BY_MAIL_ACTIVE)

    def should_have_active_login_tab(self):
        assert self.is_element_present(*RosTelecomLocators_LOGIN.LOCATOR_RT_AUTH_BY_LOGIN_ACTIVE)

    def should_have_active_ls_tab(self):
        self.is_element_present(*RosTelecomLocators_LOGIN.LOCATOR_RT_AUTH_BY_LS_ACTIVE), "Таб Лицевого счета неактивный"

    def enter_login(self, login):
        email_input = self.browser.find_element(*RosTelecomLocators_LOGIN.USERNAME_LOCATOR)
        email_input.send_keys(login)
        pass_input = self.browser.find_element(*RosTelecomLocators_LOGIN.PASSWORD_LOCATOR)
        pass_input.click()

    def enter_account(self, account):
        email_input = self.browser.find_element(*RosTelecomLocators_LOGIN.USERNAME_LOCATOR)
        email_input.send_keys(account)
        pass_input = self.browser.find_element(*RosTelecomLocators_LOGIN.PASSWORD_LOCATOR)
        pass_input.click()

    def enter_phone(self, phone):
        phone_input = self.browser.find_element(*RosTelecomLocators_LOGIN.USERNAME_LOCATOR)
        phone_input.send_keys(phone)

    def enter_password(self, password):
        password_input = self.browser.find_element(*RosTelecomLocators_LOGIN.PASSWORD_LOCATOR)
        password_input.send_keys(password)

    def enter_email(self, email):
        email_input = self.browser.find_element(*RosTelecomLocators_LOGIN.USERNAME_LOCATOR)
        email_input.send_keys(email)
        pass_input = self.browser.find_element(*RosTelecomLocators_LOGIN.PASSWORD_LOCATOR)
        pass_input.click()

    def enter_ls(self, ls):
        ls_input = self.browser.find_element(*RosTelecomLocators_LOGIN.USERNAME_LOCATOR)
        ls_input.send_keys(ls)

    def click_enter_button(self):
        enter_button = self.browser.find_element(*RosTelecomLocators_LOGIN.ENTER_BUTTON_LOCATOR)
        enter_button.click()

    def click_logout_button(self):
        logout = self.browser.find_element(*RosTelecomLocators_LOGIN.EXIT_LOCATOR)
        logout.click()

    def click_account_icon(self):
        enter_button = self.browser.find_element(*RosTelecomLocators_LOGIN.ACCOUNT_ICON_LOCATOR)
        enter_button.click()

    def click_exit(self):
        enter_button = self.browser.find_element(*RosTelecomLocators_LOGIN.EXIT_LOCATOR)
        enter_button.click()

    def should_have_opened_account_page(self):
        pass

    def click_remember_me(self):
        self.find_element(RosTelecomLocators_LOGIN.LOCATOR_RT_REMEMBER_ME, time=3).click()

    def forgot_pass(self):
        self.find_element(RosTelecomLocators_LOGIN.LOCATOR_RT_FORGOT_PASS)

    def should_have_error_message(self):
        assert self.browser.find_element(*RosTelecomLocators_LOGIN.LOCATOR_ERROR_MESSAGE).text == \
               "Неверный логин или пароль"

    def bnt_click(self):
        self.bnt_click()

    def click_forgot_pass_button(self):
        assert self.is_element_present(*RosTelecomLocators_LOGIN.LOCATOR_FORGOT_PASS)


















