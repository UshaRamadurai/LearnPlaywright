import pytest
from playwright.sync_api import Page, BrowserContext, expect

docs_URL = "https://playwright.dev/docs/intro"

@pytest.fixture(autouse=True)
def trace_generator(context:BrowserContext):
    context.tracing.start(
        name = "trace",
        screenshots=True,
        snapshots=True,
        sources=True
    )
    yield
    context.tracing.stop(path="trace.zip")

def test_page_has_get_started_link(page: Page):
    page.goto("https://playwright.dev/")
    get_started_link = page.get_by_role("link", name="GET STARTED")
    get_started_link.click()

    #assert page.url == docs_URL
    expect(page).to_have_url(docs_URL)
    expect(get_started_link).to_be_visible()