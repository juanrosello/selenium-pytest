
import pytest
import selenium.webdriver


@pytest.fixture
def browser():

    # Initialize the ChromeDriver instance:
    c = selenium.webdriver.Chrome()

    # Make its calls wait up to 10 seconds for elements to appear
    c.implicitly_wait(10)

    # Return the WebDriver instance for the setup
    yield c

    # Quite the WebDriver instance for the cleanup
    c.quit()
