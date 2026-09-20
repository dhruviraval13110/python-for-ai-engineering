"""Chapter 11: composition with dataclasses."""

from dataclasses import dataclass

@dataclass(frozen=True)
class ModelConfig:
    name: str
    threshold: float = 0.5

@dataclass
class Predictor:
    config: ModelConfig

    def predict(self, score: float) -> bool:
        return score >= self.config.threshold

print(Predictor(ModelConfig("demo", .7)).predict(.8))
