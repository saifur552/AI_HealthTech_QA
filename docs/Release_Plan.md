# Software Release Strategy & Life Cycle Plan (HealthTech SQA)

## 1. Overview
This document outlines the Alpha and Beta release strategies for the Cura Healthcare automated testing framework, ensuring strict quality gates before production deployment.

---

## 2. Alpha Release Strategy (Internal & White-Box Phase)
* **Objective:** Verify core logic integrity, internal code structure, and business rules before UI integration.
* **Activities:**
  * **Unit Testing:** Executed via `PyTest` on core calculation and alert modules (`core_logic/`).
  * **Code Coverage Analysis:** Enforced using `pytest-cov` to maintain minimum 90%+ statement and branch coverage.
  * **Mutation Testing:** Executed via `mutmut` to challenge test suite robustness by injecting artificial source code mutations.
* **Exit Criteria:** Zero unit test failures, 0 remaining unmutated survivable mutants, and approved code review.

---

## 3. Beta Release Strategy (Staging & Black-Box Phase)
* **Objective:** Validate end-to-end user journeys, system responsiveness, and third-party API integrations in a simulated production environment.
* **Activities:**
  * **UI Automation Testing:** Automated execution of 15+ critical user scenarios using Selenium WebDriver and Page Object Model (POM).
  * **Performance & Load Testing:** Benchmarking site load times and concurrent virtual user thresholds.
  * **AI-Powered Defect Logging:** Automatic generation of structured bug reports via OpenRouter LLM upon test script failure (specifically targeting the Past Date booking business logic flaw).
  * **CI/CD Continuous Testing:** Automated pipeline execution on every push using GitHub Actions.
* **Exit Criteria:** Successful execution of the automated regression suite, resolution or documentation of identified logical defects, and generation of final Allure executive reports.