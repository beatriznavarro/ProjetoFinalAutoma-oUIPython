import pytest
from pages.MenuPage import MenuPage

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Choose browser")

@pytest.fixture
def select_browser(request):
     return request.config.getoption("--browser").lower()


@pytest.fixture
def setup(select_browser):
    menu_page = MenuPage(browser=select_browser)
    yield menu_page

@pytest.fixture()
def run_all_browser(all_browser):
    menu_page = MenuPage(browser=all_browser)
    yield menu_page
