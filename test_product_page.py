# используется для генерации уникального email
import time

# фреймворк для автотестов
import pytest

# Page Object страницы
from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage


# тесты, требующие ревью
@pytest.mark.need_review

# параметризация теста для разных promo ссылок
@pytest.mark.parametrize(
    'link',
    [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",

        # известный баг
        pytest.param(
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
            marks=pytest.mark.xfail
        ),

        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    ]
)
def test_guest_can_add_product_to_basket(browser, link):

    # открыть страницу товара
    page = ProductPage(browser, link)
    page.open()

    # добавить товар в корзину
    page.add_product_to_basket()

    # проверка сообщения об успехе
    page.should_be_success_message()

    # проверка имени товара
    page.should_be_success_message_with_product_name()

    # проверка суммы корзины
    page.should_be_basket_total_equal_product_price()


# ожидаемый провал теста
@pytest.mark.xfail()
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    page = ProductPage(browser, link)
    page.open()

    page.add_product_to_basket()

    # сообщение не должно появляться
    page.should_not_be_success_message()


# сообщение не должно появляться без добавления товара
def test_guest_cant_see_success_message(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    page = ProductPage(browser, link)
    page.open()

    page.should_not_be_success_message()


# ожидаемый провал теста
@pytest.mark.xfail()
def test_message_disappeared_after_adding_product_to_basket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    page = ProductPage(browser, link)
    page.open()

    page.add_product_to_basket()

    # сообщение должно исчезнуть
    page.should_disappear_of_success_message()


# проверка наличия ссылки логина
def test_guest_should_see_login_link_on_product_page(browser):

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    page = ProductPage(browser, link)
    page.open()

    page.should_be_login_link()


# тест требует ревью
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    page = ProductPage(browser, link)
    page.open()

    # переход на страницу логина
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)

    # проверка страницы логина
    login_page.should_be_login_page()


# тест требует ревью
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    page = ProductPage(browser, link)
    page.open()

    # переход в корзину
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)

    # корзина должна быть пустой
    basket_page.should_be_empty_basket()


# тесты для зарегистрированного пользователя
@pytest.mark.user_test
class TestUserAddToBasketFromProductPage():

    # регистрация нового пользователя перед тестом
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):

        link = "http://selenium1py.pythonanywhere.com/"

        page = MainPage(browser, link)
        page.open()

        page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)

        # уникальный email
        email = str(time.time()) + "@fakemail.org"

        password = "testpassword123"

        login_page.register_new_user(email, password)

        # проверка авторизации
        login_page.should_be_authorized_user()


    # сообщение не должно отображаться
    def test_user_cant_see_success_message(self, browser):

        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

        page = ProductPage(browser, link)
        page.open()

        page.should_not_be_success_message()


    # тест требует ревью
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):

        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

        page = ProductPage(browser, link)
        page.open()

        page.add_product_to_basket()

        page.should_be_success_message()
        page.should_be_success_message_with_product_name()
        page.should_be_basket_total_equal_product_price()