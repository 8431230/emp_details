import pytest
from employee import calculate_appraisal

@pytest.mark.parametrize("scores, expected_status", [
    ([95, 92, 98], "Eligible for Promotion"),
    ([82, 85, 88], "Exceeds Expectations"),
    ([70, 75, 68], "Meets Expectations"),
    ([55, 60, 62], "Needs Improvement"),
    ([42, 45, 48], "Performance Warning"),
    ([30, 35, 38], "Subject to Training / Review"),
])
def test_appraisal_status(scores, expected_status):
    result = calculate_appraisal("Test", "TestDept", "TestRole", scores)
    assert result["status"] == expected_status
