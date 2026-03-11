# фреймворк для запуска тестов
import pytest

# Page Object классы страниц
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


# группа тестов для гостя со страницы главной
@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):

        # ссылка на главную страницу
        link = "http://selenium1py.pythonanywhere.com/"

        # открыть главную страницу
        page = MainPage(browser, link)
        page.open()

        # перейти на страницу логина
        page.go_to_login_page()

        # создать объект страницы логина
        login_page = LoginPage(browser, browser.current_url)

        # проверить, что открыта страница логина
        login_page.should_be_login_page()


    def test_guest_should_see_login_link(self, browser):

        # ссылка на главную страницу
        link = "http://selenium1py.pythonanywhere.com/"

        # открыть страницу
        page = MainPage(browser, link)
        page.open()

        # проверить наличие ссылки на логин
        page.should_be_login_link()


# проверка, что корзина пуста при открытии с главной страницы
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):

    # ссылка на главную страницу
    link = "http://selenium1py.pythonanywhere.com/"

    # открыть страницу
    page = MainPage(browser, link)
    page.open()

    # перейти в корзину
    page.go_to_basket_page()

    # создать объект страницы корзины
    basket_page = BasketPage(browser, browser.current_url)

    # проверить, что корзина пустая
    basket_page.should_be_empty_basket()