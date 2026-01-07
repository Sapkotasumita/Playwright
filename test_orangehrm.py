import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
USERNAME = "Admin"
PASSWORD = "admin123"


@pytest.fixture(scope="session")
def browser_page():
    """Setup Playwright browser and page, teardown after tests."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page(ignore_https_errors=True)
        yield page
        browser.close()


def test_login(browser_page):
    page = browser_page
    page.goto(BASE_URL)

    # Login
    page.wait_for_selector("input[name='username']", timeout=15000)
    page.fill("input[name='username']", USERNAME)
    page.fill("input[name='password']", PASSWORD)
    page.click("button[type='submit']")

    # Wait for user dropdown as dashboard indicator
    page.wait_for_selector("p.oxd-userdropdown-name", timeout=15000)
    assert page.is_visible("p.oxd-userdropdown-name")
    page.screenshot(path="login_success.png")


def test_add_employee(browser_page):
    page = browser_page

    # Navigate to PIM → Add Employee
    page.click("span:has-text('PIM')")          # Expand PIM menu
    page.click("a:has-text('Add Employee')")    # Click Add Employee
    page.wait_for_selector("input[name='firstName']", timeout=10000)

    # Fill Add Employee form
    page.fill("input[name='firstName']", "TestFirst")
    page.fill("input[name='lastName']", "TestLast")
    page.click("button[type='submit']")

    # Verify Employee added
    page.wait_for_selector("input[name='firstName']", timeout=10000)
    first_name = page.input_value("input[name='firstName']")
    last_name = page.input_value("input[name='lastName']")
    assert first_name == "TestFirst" and last_name == "TestLast"
    page.screenshot(path="employee_added.png")


def test_logout(browser_page):
    page = browser_page

    # Open user dropdown and logout
    page.click("p.oxd-userdropdown-name")
    page.click("a:has-text('Logout')")

    # Wait for login page
    page.wait_for_selector("input[name='username']", timeout=10000)
    assert page.is_visible("input[name='username']")
    page.screenshot(path="logout_success.png")
