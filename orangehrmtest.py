from playwright.sync_api import sync_playwright

def test_orangehrm_workflow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page(ignore_https_errors=True)

        # Go to latest OrangeHRM demo login page
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Login
        page.wait_for_selector("input[name='username']", timeout=15000)
        page.fill("input[name='username']", "Admin")
        page.fill("input[name='password']", "admin123")
        page.click("button[type='submit']")

        # Wait for stable element after login (user dropdown)
        page.wait_for_selector("p.oxd-userdropdown-name", timeout=15000)
        print(" Login successful")
        page.screenshot(path="orangehrm_after_login.png")

        # Navigate to PIM → Add Employee
        page.click("a[href='/web/index.php/pim/viewPimModule']")
        page.click("a[href='/web/index.php/pim/addEmployee']")
        page.wait_for_selector("input[name='firstName']", timeout=10000)

        #  Fill Add Employee form
        page.fill("input[name='firstName']", "TestFirst")
        page.fill("input[name='lastName']", "TestLast")
        page.click("button[type='submit']")

        #  Verify Employee added (check first and last name fields)
        page.wait_for_selector("input[name='firstName']", timeout=10000)
        first_name = page.input_value("input[name='firstName']")
        last_name = page.input_value("input[name='lastName']")
        if first_name == "TestFirst" and last_name == "TestLast":
            print(" Employee added successfully")
        else:
            print(" Employee add failed")
        page.screenshot(path="orangehrm_employee_added.png")

        #  Log out
        page.click("p.oxd-userdropdown-name")
        page.click("a[href='/web/index.php/auth/logout']")
        page.wait_for_selector("input[name='username']", timeout=10000)
        print(" Logout successful")
        page.screenshot(path="orangehrm_after_logout.png")

        browser.close()
        print(" Workflow completed successfully!")

if __name__ == "__main__":
    test_orangehrm_workflow()
