import pytest
from playwright.sync_api import Browser, Page

@pytest.fixture()
def record_video(browser:Browser):
    context = browser.new_context(record_video_dir="./Recordings/")
    page = context.new_page()
    yield page
    context.close()

def test_page_has_api_link(page:Page):

    page.goto("https://playwright.dev/python")
    theme_button = page.get_by_title("Switch between dark and light mode (currently dark mode)")
    theme_button.click()

    api_link = page.get_by_role("link", name="API",exact=True)
    api_link.click()

    assert api_link.is_visible()