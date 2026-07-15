# calculator-playwright

[![CI](https://github.com/sabrinajohanson/calculator-playwright/actions/workflows/ci.yml/badge.svg)](https://github.com/sabrinajohanson/calculator-playwright/actions/workflows/ci.yml)

A web calculator built with HTML, CSS and JavaScript, covered with end-to-end tests using **Python + Playwright**.

---

## Project structure

```
calculator-playwright/
├── calculator/
│   ├── index.html          # Calculator interface
│   ├── calculator.js       # Business logic
│   └── style.css           # Visual style
├── tests/
│   └── test_calculator.py  # E2E tests
├── requirements.txt
└── README.md
```

---

## How to run the tests

### 1. Install dependencies

```bash
pip install -r requirements.txt
python -m playwright install chromium
```

### 2. Run all tests

```bash
python -m pytest tests/ -v
```

### 3. Run with visible browser

```bash
python -m pytest tests/ -v --headed
```

### 4. Run with HTML report

```bash
python -m pytest tests/ -v --headed --html=report.html
```

## Test reports

Every push automatically publishes a full [Allure Report](https://sabrinajohanson.github.io/calculator-playwright/) with the detailed results of the test suite (suites, timeline, and per-test steps).

---

## Test coverage

| Group | Cases |
|---|---|
| Basic operations | Addition, subtraction, multiplication, division, decimal |
| Display | Initial state, real-time update, history |
| Clear | C button, backspace one digit at a time, backspace on result |
| Chained operations | Sequence of operations, operator change |
| Special functions | Percentage, sign toggle, decimal point |

---

## Bugs found during development

| # | Bug | Root cause | Status |
|---|---|---|---|
| [#1](https://github.com/sabrinajohanson/calculator-playwright/issues/1) | AC button not working | `clear()` is a reserved word in JavaScript | ✅ Fixed |
| [#2](https://github.com/sabrinajohanson/calculator-playwright/issues/2) | Chained operations not accumulating | `operator()` was overwriting state instead of accumulating | ✅ Fixed |
| [#3](https://github.com/sabrinajohanson/calculator-playwright/issues/3) | History showing only last two numbers | `history` variable was being overwritten on every click | ✅ Fixed |
| [#4](https://github.com/sabrinajohanson/calculator-playwright/issues/4) | Percent calculating value instead of percentage | `percent()` was always dividing by 100 regardless of context | ✅ Fixed |
| [#5](https://github.com/sabrinajohanson/calculator-playwright/issues/5) | Numbers losing precision after 15 digits | JavaScript IEEE 754 floating point limitation | ✅ Fixed |
| [#6](https://github.com/sabrinajohanson/calculator-playwright/issues/6) | Backspace blocked after pressing equals | Early return when `justCalculated` was true | ✅ Fixed |

---

## Known limitations

- Numbers are limited to 15 digits (JavaScript IEEE 754 floating point precision)
- Decimal separator is a dot `.` (international standard)
- Thousand separator is not supported

---

## Stack

- Python 3.11+
- Playwright 1.60
- Pytest + pytest-playwright
- pytest-html (test reports)