from employee import calculate_average, assign_appraisal_status

# -------------------- ELIGIBLE FOR PROMOTION TEST CASES --------------------

def test_promotion_lower_boundary():
    avg = calculate_average(90, 90, 90)
    assert assign_appraisal_status(avg) == "Eligible for Promotion"

def test_promotion_middle_value():
    avg = calculate_average(95, 95, 95)
    assert assign_appraisal_status(avg) == "Eligible for Promotion"

def test_promotion_upper_boundary():
    avg = calculate_average(100, 100, 100)
    assert assign_appraisal_status(avg) == "Eligible for Promotion"


# -------------------- EXCEEDS EXPECTATIONS TEST CASES --------------------

def test_exceeds_expectations_lower_boundary():
    avg = calculate_average(80, 80, 80)
    assert assign_appraisal_status(avg) == "Exceeds Expectations"

def test_exceeds_expectations_middle_value():
    avg = calculate_average(85, 85, 85)
    assert assign_appraisal_status(avg) == "Exceeds Expectations"

def test_exceeds_expectations_upper_boundary():
    avg = calculate_average(89.99, 89.99, 89.99)
    assert assign_appraisal_status(avg) == "Exceeds Expectations"


# -------------------- MEETS EXPECTATIONS TEST CASES --------------------

def test_meets_expectations_lower_boundary():
    avg = calculate_average(65, 65, 65)
    assert assign_appraisal_status(avg) == "Meets Expectations"

def test_meets_expectations_middle_value():
    avg = calculate_average(70, 70, 70)
    assert assign_appraisal_status(avg) == "Meets Expectations"

def test_meets_expectations_upper_boundary():
    avg = calculate_average(79.99, 79.99, 79.99)
    assert assign_appraisal_status(avg) == "Meets Expectations"


# -------------------- NEEDS IMPROVEMENT TEST CASES --------------------

def test_needs_improvement_lower_boundary():
    avg = calculate_average(50, 50, 50)
    assert assign_appraisal_status(avg) == "Needs Improvement"

def test_needs_improvement_middle_value():
    avg = calculate_average(55, 55, 55)
    assert assign_appraisal_status(avg) == "Needs Improvement"

def test_needs_improvement_upper_boundary():
    avg = calculate_average(64.99, 64.99, 64.99)
    assert assign_appraisal_status(avg) == "Needs Improvement"


# -------------------- PERFORMANCE WARNING TEST CASES --------------------

def test_performance_warning_lower_boundary():
    avg = calculate_average(40, 40, 40)
    assert assign_appraisal_status(avg) == "Performance Warning"

def test_performance_warning_middle_value():
    avg = calculate_average(45, 45, 45)
    assert assign_appraisal_status(avg) == "Performance Warning"

def test_performance_warning_upper_boundary():
    avg = calculate_average(49.99, 49.99, 49.99)
    assert assign_appraisal_status(avg) == "Performance Warning"


# -------------------- SUBJECT TO TRAINING / REVIEW TEST CASES --------------------

def test_training_review_below_40():
    avg = calculate_average(30, 35, 39)
    assert assign_appraisal_status(avg) == "Subject to Training / Review"
