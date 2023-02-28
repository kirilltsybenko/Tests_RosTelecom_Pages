import pytest
from pages.registration_page import RosTelecomLocators_REGISTRATION


@pytest.mark.registration
def test_open_registration_page(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_REGISTRATION(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()

    page2 = RosTelecomLocators_REGISTRATION(browser,browser.current_url)
    # проверяем, что открылась страница регистрации
    page2.should_be_message_about_registration()

@pytest.mark.registration
def test_that_all_forms_are_presented_on_registration_page(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_REGISTRATION(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = RosTelecomLocators_REGISTRATION(browser, browser.current_url)
    # проверяем, что открылась страница регистрации
    page2.should_be_message_about_registration()
    # проверяем что на странице регистрации есть поля
    # для ввода данных пользователя (имя,фамилия,регион,имеил или телефон, пароль, подтверждение пароля)
    page2.should_be_name_surname_login_password_confirm_password_forms()

@pytest.mark.registration
def test_that_there_is_logo(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_REGISTRATION(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = RosTelecomLocators_REGISTRATION(browser, browser.current_url)
    # проверяем что на странице есть лого
    page2.if_there_is_logo()

@pytest.mark.registration
def test_show_error_message_when_name_is_entered_not_in_сyrillic(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_REGISTRATION(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = RosTelecomLocators_REGISTRATION(browser, browser.current_url)
    name = "Kirill"
    # вводим имя латиницей в поле Имя
    page2.enter_first_name(name)
     # проверяем что появилась надпись "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    page2.should_have_name_error_message()

@pytest.mark.registration
def test_show_error_message_when_surname_is_entered_not_in_сyrillic(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_REGISTRATION(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = RosTelecomLocators_REGISTRATION(browser, browser.current_url)
    surname = "Tsybenko"
    # вводим фамилию латиницей в поле Имя
    page2.enter_last_name(surname)
     # проверяем что появилась надпись "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    page2.should_have_surname_error_message()

@pytest.mark.registration
def test_show_error_message_when_password_shorter_then_8_symbols(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_REGISTRATION(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = RosTelecomLocators_REGISTRATION(browser, browser.current_url)
    password = "1erT4"
    # вводим пароль в поле Пароль длиной 5 символов
    page2.enter_password(password)
    # проверяем что появилась надпись "Длина пароля должна быть не менее 8 символов"
    page2.should_have_error_message_that_password_should_be_more_then_8_symbols()

@pytest.mark.registration
def test_show_error_message_when_password_does_not_contain_capital_letters(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_REGISTRATION(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = RosTelecomLocators_REGISTRATION(browser, browser.current_url)
    name = "Kirill"
    password = "1ghu"
    # вводим пароль в поле Пароль без заглавных букв
    page2.enter_password(password)
    # проверяем что появилась надпись "Пароль должен содержать хотя бы одну заглавную букву"
    page2.should_have_error_message_that_password_does_not_contain_capital_letters()

@pytest.mark.registration
def test_show_error_message_when_password_does_not_contain_small_letters(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_REGISTRATION(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = RosTelecomLocators_REGISTRATION(browser, browser.current_url)
    name = "Kirill"
    password = "GHT5"
    # вводим пароль в поле Пароль без строчных букв
    page2.enter_password(password)
    # проверяем что появилась надпись "Пароль должен содержать хотя бы одну заглавную букву"
    page2.should_have_error_message_that_password_does_not_contain_small_letters()

@pytest.mark.registration
def test_show_error_message_when_password_contains_cyrillic_letters(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_REGISTRATION(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = RosTelecomLocators_REGISTRATION(browser, browser.current_url)
    name = "Kirill"
    password = "ghМосква"
    # вводим пароль в поле Пароль без заглавных букв
    page2.enter_password(password)
    # проверяем что появилась надпись "Пароль должен содержать только латинские буквы"
    page2.should_have_error_message_that_password_must_contain_only_latin_letters()

@pytest.mark.registration
def test_show_error_message_when_password_and_confirmation_password_dont_match(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_REGISTRATION(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = RosTelecomLocators_REGISTRATION(browser, browser.current_url)
    password = "QwertY321"
    confirm_password = "QwertY345"
    # вводим пароль в поле Пароль
    page2.enter_password(password)
    # вводим не совпадающий с первым пароль в поле Подтвердить пароль
    page2.enter_confirmation_of_password(confirm_password)
    # нажимаем кнопку Зарегистрироваться
    page2.click_enter_reg_button()
    # проверяем что появилась надпись "Пароли не совпадают"
    page2.should_have_error_message_that_passwords_dont_match()

@pytest.mark.registration
def test_register_new_user(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_REGISTRATION(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = RosTelecomLocators_REGISTRATION(browser, browser.current_url)
    password = "Elex2097Yh"
    first_name = "Михаил"
    last_name = "Михайлов"
    email = "mihaahim12bN@gmail.com"
    # Регистрируем нового пользователя
    page2.register_new_user(first_name, last_name, email, password)
    page2.click_enter_reg_button()
    # проверяем что новый пользователь успешно прошел Регистрацию
    page2.should_have_message_to_confirm_email_of_new_user()

@pytest.mark.registration
def test_register_new_user_that_already_exists(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_REGISTRATION(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = RosTelecomLocators_REGISTRATION(browser, browser.current_url)
    password = "QwertY321"
    first_name = "Кирилл"
    last_name = "Цыбенко"
    email = "kirilltsybenko@gmail.com"
    # Регистрируем нового пользователя
    page2.register_new_user(first_name, last_name, email, password)
    page2.click_enter_reg_button()
    # проверяем что появилась надпись "Учётная запись уже существует"
    page2.should_have_message_that_account_already_exists()