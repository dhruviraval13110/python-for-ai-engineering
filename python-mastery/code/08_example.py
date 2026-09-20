"""Chapter 08: defensive programming."""

class InvalidScoreError(ValueError):
    pass

def validate_score(score: float) -> float:
    if not 0 <= score <= 1:
        raise InvalidScoreError("score must be between 0 and 1")
    return score

print(validate_score(0.92))
