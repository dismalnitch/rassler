"""The one place that knows the sample rate.

Everything inside the synth counts time in samples (int). Seconds and ms only
exist at the edges, converted here.
"""

SAMPLE_RATE: int = 16_000

# Exact because SAMPLE_RATE is a multiple of 1000: every whole ms is a whole
# number of samples.
SAMPLES_PER_MS: int = SAMPLE_RATE // 1000
SECONDS_PER_SAMPLE: float = 1 / SAMPLE_RATE


def ms_to_samples(ms: int) -> int:
    return ms * SAMPLES_PER_MS


def seconds_to_samples(seconds: float) -> int:
    return round(seconds * SAMPLE_RATE)


def samples_to_seconds(n: int) -> float:
    return n / SAMPLE_RATE


def samples_to_ms(n: int) -> float:
    return n / SAMPLES_PER_MS
