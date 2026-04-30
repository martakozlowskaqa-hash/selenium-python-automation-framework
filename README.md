# SauceDemo Test Automation Project

## Author
Marta Kozlowska

---

## Project Overview
This project is an automated test script for the SauceDemo web application, 
created using Python, Selenium WebDriver, and Pytest.


The framework was designed to test e-commerce functionalities, 
including user authentication, inventory validation, shopping cart operations, 
and checkout processes.

---

## Features Tested

### Login
- Valid login with correct credentials
- Invalid login with incorrect credentials
- Locked out user login verification

### Inventory Page
- Product visibility verification
- Product name and price validation
- Add to Cart button behavior
- Cart badge visibility

### Cart
- Adding single product to cart
- Adding multiple products to cart
- Removing products from cart
- Cart persistence after navigation

### Checkout
- Successful checkout with valid data
- Validation for missing First Name
- Validation for missing Last Name
- Validation for missing Postal Code

---

## Technologies Used
- Python
- Pytest
- Selenium WebDriver
- Page Object Model (POM)
- Faker

---

## Supported Browsers
- Google Chrome
- Mozilla Firefox

---

## Project Structure

```
project/
│
├── pages/          # Page Object classes
├── tests/          # Test cases
├── utils/          # Test data, Faker, Driver Factory
├── conftest.py     # Pytest fixtures and setup
└── README.md