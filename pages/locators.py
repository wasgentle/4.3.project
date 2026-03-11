# используется для указания типа локатора
from selenium.webdriver.common.by import By


class BasePageLocators():

    # ссылка на страницу логина
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    # невалидный локатор (для тестов)
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    # кнопка перехода в корзину
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn-default")

    # иконка авторизованного пользователя
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():

    # форма входа
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    # форма регистрации
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    # поле email
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")

    # поле ввода пароля
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")

    # поле подтверждения пароля
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")

    # кнопка регистрации
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():

    # кнопка добавления товара в корзину
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    # название товара
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")

    # цена товара
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    # сообщение об успешном добавлении товара
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child .alertinner strong")

    # сообщение с суммой корзины
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")


class BasketPageLocators():

    # список товаров в корзине
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")

    # сообщение о пустой корзине
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")