# Cura Healthcare Service - Comprehensive Test Cases & Execution Report
**Project Target:** HealthTech Domain UI & Functional Testing  
**Framework:** Selenium WebDriver, PyTest, AI Bug Reporting  

---

## 1. Login & Security Test Cases

| Test Case ID | Test Scenario | Steps to Reproduce | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC_L01** | Valid User Login | 1. Navigate to URL<br>2. Enter valid Username & Password<br>3. Click Login | User successfully logs in and lands on Appointment page | Landed on Appointment page | **Pass** ✅ |
| **TC_L02** | Invalid Password Login | 1. Navigate to URL<br>2. Enter valid Username & incorrect Password<br>3. Click Login | System should display error message for invalid credentials | Error message displayed | **Pass** ✅ |
| **TC_L03** | Invalid Username Login | 1. Navigate to URL<br>2. Enter incorrect Username & valid Password<br>3. Click Login | System should display login failure warning | Warning message displayed | **Pass** ✅ |
| **TC_L04** | Blank Fields Validation | 1. Navigate to URL<br>2. Keep username & password empty<br>3. Click Login | Browser or application validation popup/error should occur | Validation warning triggered | **Pass** ✅ |

---

## 2. Appointment Booking Functional Test Cases

| Test Case ID | Test Scenario | Steps to Reproduce | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC_B01** | Standard Appointment Booking | 1. Login to system<br>2. Select Facility, Check Readmission, Select Program, Pick Future Date, Add comment<br>3. Click Book Appointment | Appointment confirmation page displays with correct details | Confirmation page displayed correctly | **Pass** ✅ |
| **TC_B02** | Booking without Hospital Readmission | 1. Login<br>2. Uncheck Readmission checkbox<br>3. Fill remaining fields and book | Booking should process successfully without readmission flag | Processed successfully | **Pass** ✅ |
| **TC_B03** | **Past Date Booking (Logical Bug)** | 1. Login<br>2. Select a date from the past (e.g., 2020-01-01)<br>3. Click Book Appointment | **System must restrict past dates and show error** | **System accepts past date without restriction** | **Fail ❌ (AI Bug Triggered)** |
| **TC_B04** | Blank Date Field Submission | 1. Login<br>2. Leave Visit Date field empty<br>3. Click Book Appointment | System should throw required field validation error | Error thrown successfully | **Pass** ✅ |
| **TC_B05** | Healthcare Program Radio Selection | 1. Login<br>2. Test selecting Medicaid, Medicare, and None options | Radio buttons should be mutually exclusive and functional | Working as expected | **Pass** ✅ |

---

## 3. Navigation & UI Test Cases

| Test Case ID | Test Scenario | Steps to Reproduce | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC_N01** | Home 'Make Appointment' Button | 1. Go to Home page<br>2. Click 'Make Appointment' CTA | Redirects to login page if unauthenticated | Redirected successfully | **Pass** ✅ |
| **TC_N02** | Sidebar Menu Toggle | 1. Click hamburger menu icon | Sidebar slides out displaying navigation links | Sidebar functional | **Pass** ✅ |
| **TC_N03** | History Page Verification | 1. Complete booking<br>2. Navigate to History section | Previously booked appointments should be listed | Appointment listed | **Pass** ✅ |
| **TC_N04** | Profile Page Rendering | 1. Open Profile from sidebar | User profile details render correctly | Rendered properly | **Pass** ✅ |
| **TC_N05** | Footer Social Links | 1. Scroll to footer<br>2. Click social media icons | External links should open correctly | Links valid | **Pass** ✅ |

---

## 4. End Flow Test Case

| Test Case ID | Test Scenario | Steps to Reproduce | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC_E01** | Logout Functionality | 1. Login<br>2. Open menu and click Logout | User session terminates and returns to homepage | Returned to homepage | **Pass** ✅ |