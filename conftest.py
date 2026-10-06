import pytest
from config.config import Config


@pytest.fixture(scope="session")
def base_url():
    # page.goto("/") opens https://<orgname>.app-stage.tachyoncare.io/
    return Config.BASE_URL


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "viewport": {"width": 1920, "height": 1080}}