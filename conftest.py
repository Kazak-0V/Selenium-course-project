import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="en",
        help="Язык интерфейса: en, es, fr и т.д."
    )


@pytest.fixture(scope="function")
def browser(request):
    # 1. Читаем язык из командной строки
    user_language = request.config.getoption("language")

    # 2. Настраиваем Chrome с нужным языком
    options = Options()
    options.add_experimental_option(
        "prefs", {"intl.accept_languages": user_language}
    )

    # 3. Создаём драйвер Chrome с этими настройками
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()