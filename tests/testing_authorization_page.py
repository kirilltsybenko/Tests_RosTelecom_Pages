import pytest
from pages.authorization_page import RosTelecomLocators_LOGIN
from pages.password_recovery_page import RosTelecomLocators_RECOVERY


@pytest.mark.authorization
def test_open_authorization_page(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_LOGIN(browser, link,)
    # открываем страницу авторизации
    page.open()
    # проверяем что открылась именно страница авторизации
    page.open_site()

@pytest.mark.authorization
def test_that_phone_tab_is_on_page(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_LOGIN(browser, link)
    # открываем страницу авторизации
    page.open()
    # проверяем что на странице присутствуют табы: телефон
    page.authorization_by_phone()

@pytest.mark.authorization
def test_that_mail_tab_is_on_page(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_LOGIN(browser, link)
    # открываем страницу авторизации
    page.open()
    # проверяем что на странице присутствуют табы: почта
    page.authorizations_by_mail()

@pytest.mark.authorization
def test_that_login_tab_is_on_page(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_LOGIN(browser, link)
    # открываем страницу авторизации
    page.open()
    # проверяем что на странице присутствуют табы: логин
    page.authorizations_by_login()

@pytest.mark.authorization
def test_that_ls_tab_is_on_page(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_LOGIN(browser, link)
    # открываем страницу авторизации
    page.open()
    # проверяем что на странице присутствуют табы: лицевой счет
    page.authorizations_by_ls()

@pytest.mark.authorization
def test_find_logo(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_LOGIN(browser, link)
    # открываем страницу авторизации
    page.open()
    # проверяем что на странице есть лого
    page.if_there_is_logo()

@pytest.mark.authorization
def test_phone_tab_is_active_after_filling(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_LOGIN(browser, link)
    # открываем страницу авторизации
    page.open()
    phone = "+79639759125"
    # вводим телефон в поле авторизации
    page.enter_phone(phone)
    # проверяем что таб телефона стал активным
    page.should_have_active_phone_tab()

@pytest.mark.authorization
def test_email_tab_is_active_after_filling(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_LOGIN(browser, link)
    # открываем страницу авторизации
    page.open()
    email = "kirilltsybenko@gmail.com"
    # вводим почту в поле авторизации
    page.enter_email(email)
    # проверяем что таб Почты стал активным
    page.should_have_active_email_tab()

@pytest.mark.authorization
def test_login_tab_is_active_after_filling(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_LOGIN(browser, link)
    # открываем страницу авторизации
    page.open()
    login = "KirTsy1"
    # вводим логин в поле авторизации
    page.enter_login(login)
    # проверяем что таб Логин стал активным
    page.should_have_active_login_tab()

@pytest.mark.authorization
def test_ls_tab_is_active_after_filling(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_LOGIN(browser, link)
    # открываем страницу авторизации
    page.open()
    ls = "123456789000"
    # вводим лицевой счет в поле авторизации
    page.enter_ls(ls)
    # проверяем что таб Почты стал активным
    page.should_have_active_ls_tab()
    # "Таб Лицевого счета неактивный"

@pytest.mark.authorization
def test_success_authorization_by_email(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_LOGIN(browser, link)
    # открываем страницу авторизации
    page.open()
    email = "kirilltsybenko@gmail.com"
    password = "QwertY321"
    # вводим телефон в поле авторизации
    page.enter_email(email)
    # вводим пароль в поле авторизации
    page.enter_password(password)
    # нажимаем кнопку Войти
    page.click_enter_button()
    # проверяем что открылась страница личного кабинета
    page.should_have_opened_account_page()
    # выходим из аккаунта
    page.click_logout_button()

@pytest.mark.authorization
def test_show_error_message_when_there_is_wrong_email_or_password(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_LOGIN(browser, link)
    # открываем страницу авторизации
    page.open()

    email = "kirilltsybenko@gmail.com"
    password = "QwertY333"
    # вводим имеил в поле авторизации
    page.enter_email(email)
    # вводим неверный пароль в поле авторизации
    page.enter_password(password)
    # нажимаем кнопку Войти
    page.click_enter_button()
    # проверяем что появилась надпись "Неверный логин или пароль"
    page.should_have_error_message()

@pytest.mark.authorization
def test_show_error_message_when_there_is_wrong_login_or_password(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_LOGIN(browser, link)
    # открываем страницу авторизации
    page.open()

    login = "Kirtsy123"
    password = "ghjT4535"
    # вводим логин в поле авторизации
    page.enter_login(login)
    # вводим неверный пароль в поле авторизации
    page.enter_password(password)
    # нажимаем кнопку Войти
    page.click_enter_button()
    # проверяем что появилась надпись "Неверный логин или пароль"
    page.should_have_error_message()

@pytest.mark.authorization
def test_recovery_password_page_open(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_LOGIN(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Забыл пароль
    page.click_forgot_pass_button()
    page2 = RosTelecomLocators_RECOVERY(browser, browser.current_url)
    # проверяем, что открылась страница восстановления пароля
    page2.should_be_message_about_password_recovery()

@pytest.mark.authorization
def test_that_phone_email_login_account_tabs_are_presented_on_recovery_password_page(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_LOGIN(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Забыл пароль
    page.click_forgot_pass_button()
    page2 = RosTelecomLocators_RECOVERY(browser, browser.current_url)
    # проверяем что на странице присутствуют табы: телефон, почта, логин, лицевой счет
    page2.should_have_tabs()


@pytest.mark.authorization
def test_that_recovery_password_page_has_login_form(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_LOGIN(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Забыл пароль
    page.click_forgot_pass_button()
    page2 = RosTelecomLocators_RECOVERY(browser, browser.current_url)
    # проверяем, что есть форма для ввода данных
    page2.should_be_login_form()

@pytest.mark.authorization
def test_that_recovery_password_page_has_captcha(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = RosTelecomLocators_LOGIN(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Забыл пароль
    page.click_forgot_pass_button()
    page2 = RosTelecomLocators_RECOVERY(browser, browser.current_url)
    # проверяем, есть ли поле Каптча
    page2.should_have_captcha()