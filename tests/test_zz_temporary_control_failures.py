"""TEMPORARY control tests, created to validate the Teams notification's failure classification logic (automation vs. functional issue). Remove this file once validation is complete."""


def test_zz_temporary_control_automation_issue():
    # Intentionally fails with a message that should be classified as a likely automation issue by the keyword-based heuristic.
    assert False, "Timeout waiting for element to become visible"


def test_zz_temporary_control_functional_issue():
    # Intentionally fails with a message that should be classified as a likely functional issue (a real assertion mismatch).
    assert 2 + 2 == 5, "Expected calculator result did not match"