AI-Powered QA Automation Suite (Cura Healthcare)
========================================

Overview
--------
This is a SQA Automation Framework built for the Katalon CURA Healthcare application.
It ensures system reliability through a complete testing lifecycle, from core logic validation to advanced AI-driven defect reporting.

Key Features
------------
- Manual Testing: Documented test cases with real execution reports for baseline quality.
- Unit Testing: White-box testing for core billing logic and exact decimal rounding.
- Mutation Testing: Fault injection that scored 100 percent against surviving mutants.
- UI Automation: Page Object Model design for clean and maintainable browser interactions.
- API Testing: Direct backend validation and response time checks without GUI overhead.
- Performance Testing: Simulated load testing using Locust to check server limits.
- AI Bug Reporter: Automated Jira-style bug ticket generation using OpenRouter API.
- CI/CD Pipeline: Continuous integration via GitHub Actions running in headless mode.

Tools Used
----------
- Python
- Selenium WebDriver
- Pytest and Pytest-HTML
- Requests
- Locust
- Mutmut
- GitHub Actions
- OpenRouter API

How to Run
----------
Clone the repository, install the requirements, and set your OpenRouter API key in the environment variables.
Run the pytest command for functional tests, or run the locust command for performance testing.