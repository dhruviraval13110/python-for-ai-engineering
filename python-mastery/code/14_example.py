"""Chapter 14: testable code."""

def normalize_score(score: float) -> float:
    if not 0 <= score <= 100:
        raise ValueError("score must be 0..100")
    return score / 100

assert normalize_score(75) == 0.75
