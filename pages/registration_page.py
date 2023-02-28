from tests.base_page import PageBase
from tests.base_page import PageBaseLocators
from selenium.webdriver.common.by import By


class RosTelecomLocators_REGISTRATION(PageBase, PageBaseLocators):
    LOCATOR_RT_REG_FIRST_NAME = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/div/input")
    LOCATOR_RT_REG_LAST_NAME = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input")
    LOCATOR_RT_REG_REGION = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/div/input")
    LOCATOR_RT_REG_EMAIL_PHONE = (By.ID, "address")
    LOCATOR_RT_REG_PASS = (By.ID, "password")
    LOCATOR_RT_REG_CONFIRM_PASS = (By.ID, "password-confirm")
    LOCATOR_RT_REG_REGISTRATION = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/button")
    LOCATOR_FIRST_NAME_ERROR_MESSAGE = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span')
    LOCATOR_LAST_NAME_ERROR_MESSAGE = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
    LOCATOR_PASSWORD_ERROR_MESSAGE = (By.ID, 'page-right')
    LOCATOR_PASSWORD_CONFIRM_ERROR_MESSAGE = (By.ID, 'page-right')
    LOCATOR_LOGO = (By.CSS_SELECTOR, '.main-header__logo')
    LOCATOR_REGISTER = (By.CSS_SELECTOR, '#page-right > div > div > div > form > button')
    LOCATOR_REGISTRATION_BUTTON = (By.ID, 'kc-register')
    LOCATOR_REGISTRATION_MESSAGE = (By.CSS_SELECTOR, '.card-container__title')
    LOCATOR_MESSAGE_THAT_ACCOUNT_ALREADY_EXISTS = (By.CLASS_NAME, 'card-modal__title')
    LOCATOR_MESSAGE_TO_CONFIRM_EMAIL = (By.CSS_SELECTOR, '.card-container__title')


    def click_registration_button(self):
        registration_button = self.browser.find_element(*RosTelecomLocators_REGISTRATION.LOCATOR_REGISTRATION_BUTTON)
        registration_button.click()

    def click_enter_reg_button(self):
        enter_reg_button = self.browser.find_element(*RosTelecomLocators_REGISTRATION.LOCATOR_REGISTER)
        enter_reg_button.click()

    def should_be_message_about_registration(self):
        self.is_element_present(*RosTelecomLocators_REGISTRATION.LOCATOR_REGISTRATION_MESSAGE), \

    def enter_first_name(self, first_name):
        first_name_input = self.browser.find_element(*RosTelecomLocators_REGISTRATION.LOCATOR_RT_REG_FIRST_NAME)
        first_name_input.send_keys(first_name)
        last_name_input = self.browser.find_element(*RosTelecomLocators_REGISTRATION.LOCATOR_RT_REG_LAST_NAME)
        last_name_input.click()

    def enter_last_name(self, last_name):
        last_name_input = self.browser.find_element(*RosTelecomLocators_REGISTRATION.LOCATOR_RT_REG_LAST_NAME)
        last_name_input.send_keys(last_name)
        first_name_input = self.browser.find_element(*RosTelecomLocators_REGISTRATION.LOCATOR_RT_REG_FIRST_NAME)
        first_name_input.click()

    def enter_email(self, email):
        password_input = self.browser.find_element(*RosTelecomLocators_REGISTRATION.LOCATOR_RT_REG_EMAIL_PHONE)
        password_input.send_keys(email)
        first_name_input = self.browser.find_element(*RosTelecomLocators_REGISTRATION.LOCATOR_RT_REG_FIRST_NAME)
        first_name_input.click()

    def enter_phone(self, phone):
        password_input = self.browser.find_element(*RosTelecomLocators_REGISTRATION.LOCATOR_RT_REG_EMAIL_PHONE)
        password_input.send_keys(phone)
        first_name_input = self.browser.find_element(*RosTelecomLocators_REGISTRATION.LOCATOR_RT_REG_FIRST_NAME)
        first_name_input.click()

    def enter_password(self, password):
        password_input = self.browser.find_element(*RosTelecomLocators_REGISTRATION.LOCATOR_RT_REG_PASS)
        password_input.send_keys(password)

    def enter_confirmation_of_password(self, password):
        password_input = self.browser.find_element(*RosTelecomLocators_REGISTRATION.LOCATOR_RT_REG_CONFIRM_PASS)
        password_input.send_keys(password)

    def should_have_name_error_message(self):
        assert self.browser.find_element(*RosTelecomLocators_REGISTRATION.LOCATOR_FIRST_NAME_ERROR_MESSAGE).text == \
               "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

    def should_have_surname_error_message(self):
        assert self.browser.find_element(*RosTelecomLocators_REGISTRATION.LOCATOR_LAST_NAME_ERROR_MESSAGE).text == \
               "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

    def should_have_error_message_that_password_should_be_more_then_8_symbols(self):
        var = self.browser.find_element(*RosTelecomLocators_REGISTRATION.LOCATOR_PASSWORD_ERROR_MESSAGE).text == \
               "Длина пароля должна быть не менее 8 символов"

    def should_have_error_message_that_password_does_not_contain_capital_letters(self):
        var = self.browser.find_element(*RosTelecomLocators_REGISTRATION.LOCATOR_PASSWORD_ERROR_MESSAGE).text == \
              "Пароль должен содержать хотя бы одну заглавную букву"

    def should_have_error_message_that_password_does_not_contain_small_letters(self):
        var = self.browser.find_element(*RosTelecomLocators_REGISTRATION.LOCATOR_PASSWORD_ERROR_MESSAGE).text == \
              "Пароль должен содержать хотя бы одну прописную букву"

    def should_have_error_message_that_password_must_contain_only_latin_letters(self):
        var =  self.browser.find_element(*RosTelecomLocators_REGISTRATION.LOCATOR_PASSWORD_ERROR_MESSAGE).text == \
               "Пароль должен содержать только латинские буквы"

    def should_have_error_message_that_passwords_dont_match(self):
        var =  self.browser.find_element(*RosTelecomLocators_REGISTRATION.LOCATOR_PASSWORD_CONFIRM_ERROR_MESSAGE).text == \
               "Пароли не совпадают"

    def if_there_is_logo(self):
        assert self.is_element_present(*RosTelecomLocators_REGISTRATION.LOCATOR_LOGO)

    def should_be_name_surname_login_password_confirm_password_forms(self):
        self.is_element_present(*RosTelecomLocators_REGISTRATION.LOCATOR_RT_REG_FIRST_NAME)
        self.is_element_present(*RosTelecomLocators_REGISTRATION.LOCATOR_RT_REG_LAST_NAME)
        self.is_element_present(*RosTelecomLocators_REGISTRATION.LOCATOR_RT_REG_EMAIL_PHONE)
        self.is_element_present(*RosTelecomLocators_REGISTRATION.LOCATOR_RT_REG_PASS)
        self.is_element_present(*RosTelecomLocators_REGISTRATION.LOCATOR_RT_REG_CONFIRM_PASS)

    def should_have_message_that_account_already_exists(self):
        assert self.browser.find_element(*RosTelecomLocators_REGISTRATION.LOCATOR_MESSAGE_THAT_ACCOUNT_ALREADY_EXISTS).text == \
               "Учётная запись уже существует"

    def register_new_user(self, name, surname, email, password):
        self.enter_first_name(name)
        self.enter_last_name(surname)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirmation_of_password(password)

    def should_have_message_to_confirm_email_of_new_user(self):
        assert self.browser.find_element(*RosTelecomLocators_REGISTRATION.LOCATOR_MESSAGE_TO_CONFIRM_EMAIL).text == \
               "Подтверждение email"



