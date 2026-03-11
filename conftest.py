import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # добавление параметра языка браузера
    parser.addoption(
        '--language',
        action='store',
        default='en'
    )

    # добавление параметра выбора браузера
    parser.addoption(
        '--browser_name',
        action='store',
        default='chrome'
    )


@pytest.fixture(scope="function")
def browser(request):
    # получение параметров из командной строки pytest
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")

    # настройка языковых параметров браузера
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language}
    )

    browser = None

    # запуск выбранного браузера
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options)

    else:
        # ошибка если указан неподдерживаемый браузер
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser  # передача браузера в тесты

    # закрытие браузера после выполнения теста
    print("\nquit browser..")
    browser.quit()