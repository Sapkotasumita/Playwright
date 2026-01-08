# Playwright Automation Test Suite
This repository contains **automation test scripts** for the OrangeHRM web application using **Python**, **Playwright**, and **Pytest**, including screenshots for verification.

## Tools & Technologies
- Python 3.x
- Playwright
- Pytest
- Browsers: Chromium / Firefox / WebKit
- Screenshots:Captured during test execution

## Project Structure
Playwright/
├── demo.py
├── orangehrmtest.py
├── test_example.py
├── test_orangehrm.py
├── Screenshot/
│ ├── login_success.png
│ ├── logout_success.png
│ └── employee_added.png
└── README.md

## Installation & Setup
1. Clone the repo:
git clone https://github.com/Sapkotasumita/Playwright.git
cd Playwright

Install dependencies:
pip install -r requirements.txt
# Or manually
pip install playwright pytest
Install Playwright browsers:

playwright install
Running Tests
Run all tests:

pytest
Run a specific test:

pytest test_orangehrm.py
Screenshots saved in Screenshot/
