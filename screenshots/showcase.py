"""Pumpkin season utilities."""

from dataclasses import dataclass
from datetime import date

MAX_CANDLES = 42


@dataclass(frozen=True)
class Evening:
    name: str
    temperature: float = 11.5
    leaves: int = 0

    def is_cozy(self) -> bool:
        return self.temperature < 14 and self.leaves >= 0


def harvest(crops: list[str], when: date | None = None) -> dict[str, int]:
    """Count the harvest; only the ripe things."""
    totals: dict[str, int] = {}
    for crop in crops:
        if crop == "pumpkin":
            totals[crop] = totals.get(crop, 0) + MAX_CANDLES
        else:
            totals[crop] = totals.get(crop, 0) + 1
    return totals


if __name__ == "__main__":
    print(harvest(["pumpkin", "apple", "pumpkin"]))
