from .base_page import BasePage  # базовый класс страницы


class MainPage(BasePage):  # Page Object главной страницы

    def __init__(self, *args, **kwargs):
        # инициализация через конструктор BasePage
        super(MainPage, self).__init__(*args, **kwargs)