# базовый класс страницы
from .base_page import BasePage

# локаторы элементов страницы логина
from .locators import LoginPageLocators


# Page Object страницы логина
class LoginPage(BasePage):

    def should_be_login_page(self):
        # проверка основных элементов страницы логина
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка, что в URL есть "login"
        assert "login" in self.browser.current_url, "Should be login url"

    def should_be_login_form(self):
        # проверка наличия формы входа
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "Login form is not presented"

    def should_be_register_form(self):
        # проверка наличия формы регистрации
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "Register form is not presented"

    def register_new_user(self, email, password):

        # ввод email
        email_input = self.browser.find_element(
            *LoginPageLocators.REGISTER_EMAIL
        )
        email_input.send_keys(email)

        # ввод пароля
        password1_input = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD1
        )
        password1_input.send_keys(password)

        # подтверждение пароля
        password2_input = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD2
        )
        password2_input.send_keys(password)

        # отправка формы регистрации
        register_button = self.browser.find_element(
            *LoginPageLocators.REGISTER_BUTTON
        )
        register_button.click()