from operator import truediv

import pytest
from playwright.sync_api import Browser,Page

docs_URL = "https://playwright.dev/docs/intro"

@pytest.fixture
def playwright_page(page: Page):
    page.goto("https://playwright.dev/")
    yield page
    page.close()

def test_page_has_get_started_link(playwright_page,page: Page):
    get_started_link = page.get_by_role("link", name="GET STARTED")
    get_started_link.screenshot(path="./Screenshots/getStarted.png")
    get_started_link.click()

    assert page.url == docs_URL

def test_page_has_docs_link(playwright_page,page: Page):
    docs_link = page.get_by_role("link", name="DOCS")
    docs_link.click()

    page.screenshot(path="./Screenshots/docs.png", full_page=True)
    assert docs_link.is_visible()


