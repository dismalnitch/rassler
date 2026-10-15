import math

from rassler_py.generator import Generator
from rassler_py.timing import SAMPLE_RATE


class Sine(Generator):
    """state: {"freq": Hz, "amp": peak, "phase": radians (optional)}"""

    def generate(self, n: int) -> float:
        freq = self.state["freq"]
        amp = self.state["amp"]
        phase = self.state.get("phase", 0.0)

        # Whole cycles elapsed by sample n. Only the fractional part matters,
        # and keeping the angle in [0, 2π) is what keeps f32 accurate later.
        cycles = freq * n / SAMPLE_RATE
        return amp * math.sin(2 * math.pi * (cycles % 1.0) + phase)


sine = Sine({"freq": 34, "amp": 1})
