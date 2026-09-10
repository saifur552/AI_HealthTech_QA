Manual Test Execution Report
============================

Document Version: 1.0
Tested By: Saifur Rahman
Execution Date: September 10, 2026
Environment: Windows 10, Google Chrome (Version 120.0)
Application URL: https://katalon-demo-cura.herokuapp.com/

Execution Summary
-----------------
 Every test case listed below was manually executed in the staging environment. The exact steps were followed, and actual results were observed and documented. 

Detailed Test Cases
-------------------

| TC ID | Category | Scenario | Steps to Execute | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC_001 | Auth | Valid Login | 1. Open URL <br>2. Enter valid user <br>3. Enter valid pass <br>4. Click Login | User successfully logs in and sees Appointment page. | Logged in successfully and redirected to Appointment page. | Pass |
| TC_002 | Auth | Invalid Password | 1. Enter valid user <br>2. Enter wrong pass <br>3. Click Login | Error message appears. | Login failed message displayed clearly. | Pass |
| TC_003 | Auth | Empty Fields | 1. Leave fields blank <br>2. Click Login | Login rejected. | Login rejected, no redirection happened. | Pass |
| TC_004 | Security | Direct URL Access | 1. Paste Appointment URL without login | Redirected back to login page. | Redirected to login page immediately. | Pass |
| TC_005 | Functionality | Valid Booking | 1. Login <br>2. Fill all data <br>3. Click Book | Booking confirmed. | Booking confirmed and summary page shown. | Pass |
| TC_006 | Validation | Empty Date | 1. Leave date blank <br>2. Click Book | HTML5 validation error shown. | "Please fill out this field" warning appeared. | Pass |
| TC_007 | Logic | Past Date Booking | 1. Select past date <br>2. Click Book | System rejects past date. | System accepted the past date and confirmed booking. | Fail |
| TC_008 | UI | Checkbox Toggle | 1. Check/uncheck hospital readmission | State changes visually. | Checkbox toggled without delay. | Pass |
| TC_009 | UI | Radio (Medicare) | 1. Select Medicare | Selected successfully. | Radio button selected. | Pass |
| TC_010 | UI | Radio (Medicaid) | 1. Select Medicaid | Selected, Medicare deselected. | Switched perfectly between options. | Pass |
| TC_011 | Data | Verify Confirmation | 1. Book and check summary | Data matches input exactly. | Displayed data matched user inputs. | Pass |
| TC_012 | Functionality | History (Data) | 1. Book <br>2. Go to History | Appointment is visible. | Previous appointment found in history. | Pass |
| TC_013 | Functionality | History (Empty) | 1. Login fresh <br>2. Go to History | No appointment message. | "No appointment" displayed. | Pass |
| TC_014 | Auth | Logout | 1. Click menu <br>2. Click Logout | Logged out to homepage. | Logged out and session destroyed. | Pass |
| TC_015 | UI | Sidebar Toggle | 1. Click hamburger menu | Menu slides in/out. | Menu animation worked smoothly. | Pass |

Failure Note
------------
The failure detected in TC_007 (Past Date Booking) has been marked for automation. 