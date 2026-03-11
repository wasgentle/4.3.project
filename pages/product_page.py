from .base_page import BasePage  # базовый класс страницы
from .locators import ProductPageLocators  # локаторы страницы товара


class ProductPage(BasePage):  # Page Object страницы товара

    def add_product_to_basket(self):
        # нажать кнопку добавления товара в корзину
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

        # решение промо-квиза (alert)
        self.solve_quiz_and_get_code()

    def should_be_success_message_with_product_name(self):
        # проверка, что в сообщении указано правильное название товара
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_product_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text

        assert product_name == message_product_name, \
            f"Product name in message '{message_product_name}' does not match actual product name '{product_name}'"

    def should_be_basket_total_equal_product_price(self):
        # проверка, что сумма корзины равна цене товара
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text

        assert product_price == basket_total, \
            f"Basket total '{basket_total}' does not match product price '{product_price}'"

    def should_be_success_message(self):
        # проверка появления сообщения об успешном добавлении
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented, but should be"

    def should_not_be_success_message(self):
        # проверка отсутствия сообщения
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_of_success_message(self):
        # проверка, что сообщение исчезает
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear"