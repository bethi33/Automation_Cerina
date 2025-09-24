import pytest

def categorize_phq9(score: int) -> str:
    if score <= 4:
        return "Minimal"
    elif score <= 9:
        return "Mild"
    elif score <= 14:
        return "Moderate"
    elif score <= 19:
        return "Moderately Severe"
    else:
        return "Severe"

@pytest.mark.parametrize("score, expected", [
    (0, "Minimal"),
    (4, "Minimal"),
    (5, "Mild"),
    (9, "Mild"),
    (10, "Moderate"),  
    (14, "Moderate"),
    (15, "Moderately Severe"),
    (19, "Moderately Severe"),
    (20, "Severe"),
    (27, "Severe"),
])
def test_phq9_categories(score, expected):
    assert categorize_phq9(score) == expected
    
def test_phq9_invalid_scores():
    with pytest.raises(ValueError):
        categorize_phq9(-1)
    with pytest.raises(ValueError):
        categorize_phq9(28)
    with pytest.raises(TypeError):
        categorize_phq9("ten")
    with pytest.raises(TypeError):
        categorize_phq9(None)
    with pytest.raises(TypeError):
        categorize_phq9(5.5)

