from abc import ABC, abstractmethod


class Generator(ABC):
    def __init__(self, state):
        self.state = state

    @abstractmethod
    def generate(self, n: int) -> float:
        """You gotta generate: return the sample at sample index n."""

    def generate_block(self, start: int, count: int) -> tuple[list[float], int]:
        """Samples start .. start + count - 1, plus where the next block starts."""
        end = start + count
        samples = [self.generate(n) for n in range(start, end)]
        return samples, end
