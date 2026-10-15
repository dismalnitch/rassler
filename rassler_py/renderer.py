from rassler_py.oscillators import SAMPLE_RATE_KHZ


class Renderer:
    SAMPLE_RATE_KHZ = 16

    def __init__(self):
        pass

    def sin(freq_hz: float, amp: int, time_s: float, phase_rad: float = 0) -> float:
        omega = (2 * math.pi) * freq_hz
        return amp * math.sin(omega * time_s + phase_rad)

    def render(prev_tick_ms: int, ms: int) -> tuple[Iterable[float], int]:
        sample_count = ms * SAMPLE_RATE_KHZ
        start_sample = prev_tick_ms * SAMPLE_RATE_KHZ
        end_sample = start_sample + sample_count
        tick_duration_s = (ms / sample_count) / 1000

        prev_time_s = prev_tick_ms / 1000
        cur_time_s = prev_time_s
        samples: Iterable[float] = []
        for tick in range(start_sample, end_sample):
            sample = sin(freq, 1, cur_time_s)
            samples.append(sample)
            cur_time_s += tick_duration_s
        return samples, (prev_tick_ms + ms)
