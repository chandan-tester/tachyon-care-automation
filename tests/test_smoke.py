import re
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
def test_login_page_opens(page: Page):
    page.goto("/")
    expect(page).to_have_title(re.compile("Tachyon"))
    expect(page.get_by_role("heading", name="Sign in")).to_be_visible()
    expect(page.get_by_placeholder("Password")).to_be_visible()
    expect(page.get_by_role("button", name="Sign in")).to_be_visible()