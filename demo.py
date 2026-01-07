from playwright.sync_api import sync_playwright
import time

def run_demo_test():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Go to demo website
        page.goto("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

        # Close popup if it appears
        try:
            page.click("#at-cv-lightbox-close", timeout=3000)
            print("Popup closed")
        except:
            print("No popup appeared")

        # Single Input Field Test
        message_input = page.query_selector("#user-message")
        message_input.fill("Hello Playwright!")  # Fill input
        page.click("#showInput")  # Click 'Show Message' button

        # Verify output
        output_text = page.inner_text("#display")
        print(f"Output Text: {output_text}")
        assert output_text == "Hello Playwright!", "Single input test failed!"

        # Two Input Fields Test (Sum)
        page.fill("#sum1", "10")
        page.fill("#sum2", "25")
        page.click("button[onclick='return total()']")  # Click 'Get Total' button

        # Verify sum
        sum_result = page.inner_text("#displayvalue")
        print(f"Sum Result: {sum_result}")
        assert sum_result == "35", "Sum calculation test failed!"

        # Take screenshot of the page
        page.screenshot(path="playwright_demo_test.png")
        print("Screenshot saved: playwright_demo_test.png")

        # Close browser
        browser.close()
        print("Demo test completed successfully!")

if __name__ == "__main__":
    run_demo_test()
