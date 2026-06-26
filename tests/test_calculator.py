# test_calculator.py
# End-to-end tests for the calculator using Playwright + Pytest

import pytest
from pathlib import Path
from playwright.sync_api import Page, expect

# Path to the calculator HTML file
CALCULATOR_PATH = (
    Path(__file__).parent.parent / "calculator" / "index.html"
).resolve()

# ── Fixture: opens the calculator before each test ──────────────────────────

@pytest.fixture(autouse=True)
def open_calculator(page: Page):
    page.goto(f"file:///{CALCULATOR_PATH}")
    expect(page.get_by_test_id("calculator")).to_be_visible()

# ── Helpers ──────────────────────────────────────────────────────────────────

def get_result(page: Page) -> str:
    return page.get_by_test_id("result").inner_text().strip()

def get_history(page: Page) -> str:
    return page.get_by_test_id("expression").inner_text().strip()

def click(page: Page, testid: str):
    page.get_by_test_id(testid).click()

# ── First test ───────────────────────────────────────────────────────────────

class TestBasicOperations:

    def test_addition(self, page: Page):
        """2 + 3 = 5"""
        click(page, "btn-2")
        click(page, "btn-add")
        click(page, "btn-3")
        click(page, "btn-equals")
        assert get_result(page) == "5"

    def test_subtraction(self, page: Page):
        """10 - 4 = 6"""
        click(page, "btn-1")
        click(page, "btn-0")
        click(page, "btn-subtract")
        click(page, "btn-4")
        click(page, "btn-equals")
        assert get_result(page) == "6"

    def test_multiplication(self, page: Page):
        """6 × 7 = 42"""
        click(page, "btn-6")
        click(page, "btn-multiply")
        click(page, "btn-7")
        click(page, "btn-equals")
        assert get_result(page) == "42"

    def test_division(self, page: Page):
        """15 ÷ 3 = 5"""
        click(page, "btn-1")
        click(page, "btn-5")
        click(page, "btn-divide")
        click(page, "btn-3")
        click(page, "btn-equals")
        assert get_result(page) == "5"

    def test_decimal_result(self, page: Page):
        """1 ÷ 4 = 0.25"""
        click(page, "btn-1")
        click(page, "btn-divide")
        click(page, "btn-4")
        click(page, "btn-equals")
        assert get_result(page) == "0.25"

class TestDisplay:

    def test_initial_state(self, page: Page):
        """Display shows 0 on load"""
        assert get_result(page) == "0"
        assert get_history(page) == ""

    def test_display_updates_on_digit(self, page: Page):
        """Typing 9 shows 9 on display"""
        click(page, "btn-9")
        assert get_result(page) == "9"

    def test_history_shown_after_operator(self, page: Page):
        """After typing 5 +, history shows 5 +"""
        click(page, "btn-5")
        click(page, "btn-add")
        assert "5" in get_history(page)
        assert "+" in get_history(page)

    def test_history_shown_after_equals(self, page: Page):
        """After = history shows full expression"""
        click(page, "btn-3")
        click(page, "btn-add")
        click(page, "btn-4")
        click(page, "btn-equals")
        history = get_history(page)
        assert "3" in history
        assert "4" in history
        assert "=" in history

    def test_history_clears_after_new_input(self, page: Page):
        """After = typing a new number clears history"""
        click(page, "btn-3")
        click(page, "btn-add")
        click(page, "btn-4")
        click(page, "btn-equals")
        click(page, "btn-5")
        assert get_history(page) == ""

class TestClear:

    def test_clear_resets_to_zero(self, page: Page):
        """C resets display to 0"""
        click(page, "btn-9")
        click(page, "btn-clear")
        assert get_result(page) == "0"
        assert get_history(page) == ""

    def test_clear_after_operation(self, page: Page):
        """C after incomplete operation resets everything"""
        click(page, "btn-5")
        click(page, "btn-add")
        click(page, "btn-3")
        click(page, "btn-clear")
        assert get_result(page) == "0"
        assert get_history(page) == ""

    def test_backspace_removes_last_digit(self, page: Page):
        """Backspace removes one digit at a time"""
        click(page, "btn-1")
        click(page, "btn-2")
        click(page, "btn-3")
        click(page, "btn-backspace")
        assert get_result(page) == "12"

    def test_backspace_on_result(self, page: Page):
        """Backspace works on result after equals"""
        click(page, "btn-1")
        click(page, "btn-5")
        click(page, "btn-add")
        click(page, "btn-5")
        click(page, "btn-equals")
        click(page, "btn-backspace")
        assert get_result(page) == "2"

class TestChainedOperations:

    def test_chained_addition(self, page: Page):
        """1 + 1 + 1 + 1 + 3 = 7"""
        click(page, "btn-1")
        click(page, "btn-add")
        click(page, "btn-1")
        click(page, "btn-add")
        click(page, "btn-1")
        click(page, "btn-add")
        click(page, "btn-1")
        click(page, "btn-add")
        click(page, "btn-3")
        click(page, "btn-equals")
        assert get_result(page) == "7"

    def test_chained_mixed_operations(self, page: Page):
        """10 + 5 - 3 = 12"""
        click(page, "btn-1")
        click(page, "btn-0")
        click(page, "btn-add")
        click(page, "btn-5")
        click(page, "btn-subtract")
        click(page, "btn-3")
        click(page, "btn-equals")
        assert get_result(page) == "12"

    def test_operator_change(self, page: Page):
        """5 + changed to × 3 = 15"""
        click(page, "btn-5")
        click(page, "btn-add")
        click(page, "btn-multiply")
        click(page, "btn-3")
        click(page, "btn-equals")
        assert get_result(page) == "15"

class TestSpecialFunctions:

    def test_percent_standalone(self, page: Page):
        """50% = 0.5"""
        click(page, "btn-5")
        click(page, "btn-0")
        click(page, "btn-percent")
        assert get_result(page) == "0.5"

    def test_percent_in_operation(self, page: Page):
        """100 - 56% = 44"""
        click(page, "btn-1")
        click(page, "btn-0")
        click(page, "btn-0")
        click(page, "btn-subtract")
        click(page, "btn-5")
        click(page, "btn-6")
        click(page, "btn-percent")
        click(page, "btn-equals")
        assert get_result(page) == "44"

    def test_sign_toggle(self, page: Page):
        """5 +/- = -5"""
        click(page, "btn-5")
        click(page, "btn-sign")
        assert get_result(page) == "-5"

    def test_sign_toggle_twice(self, page: Page):
        """5 +/- +/- = 5"""
        click(page, "btn-5")
        click(page, "btn-sign")
        click(page, "btn-sign")
        assert get_result(page) == "5"

    def test_decimal_input(self, page: Page):
        """1.5 displays correctly"""
        click(page, "btn-1")
        click(page, "btn-dot")
        click(page, "btn-5")
        assert get_result(page) == "1.5"

    def test_decimal_no_duplicate_dot(self, page: Page):
        """Typing dot twice does not duplicate it"""
        click(page, "btn-1")
        click(page, "btn-dot")
        click(page, "btn-dot")
        click(page, "btn-5")
        assert get_result(page).count(".") == 1