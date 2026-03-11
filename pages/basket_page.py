from .base_page import BasePage  # базовый класс со вспомогательными методами
from .locators import BasketPageLocators  # локаторы элементов страницы корзины


class BasketPage(BasePage):  # Page Object для страницы корзины

    def should_be_empty_basket(self):
        # проверка, что корзина пустая
        self.should_not_be_products_in_basket()
        self.should_be_empty_basket_message()

    def should_not_be_products_in_basket(self):
        # проверка отсутствия товаров в корзине
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket contains products, but should be empty"

    def should_be_empty_basket_message(self):
        # получение текста сообщения о пустой корзине
        empty_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text

        # проверка текста сообщения
        assert "Your basket is empty" in empty_message, \
            f"Expected 'Your basket is empty' message, got: '{empty_message}'"