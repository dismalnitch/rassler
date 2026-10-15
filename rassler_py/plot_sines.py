"""Plot oscillator output against a reference sine.

    python plot_sines.py                 # opens a window
    python plot_sines.py --freq 40 60    # several frequencies
    python plot_sines.py --save out.png  # write a file instead
"""

import argparse

import matplotlib.pyplot as plt
import numpy as np

from oscillators import SAMPLE_RATE_KHZ, sin_tick

SAMPLE_RATE = SAMPLE_RATE_KHZ * 1000


def reference_sine(freq: float, start_sample: int, count: int) -> np.ndarray:
    """A known-good sine: sample n sits at n / SAMPLE_RATE seconds."""
    n = np.arange(start_sample, start_sample + count)
    return np.sin(2 * np.pi * freq * n / SAMPLE_RATE)


def ms_axis(start_sample: int, count: int) -> np.ndarray:
    return np.arange(start_sample, start_sample + count) / SAMPLE_RATE_KHZ


def plot_one_block(ax, freq: float, ms: int) -> None:
    """One call to sin_tick, with the reference drawn underneath."""
    samples, _ = sin_tick(freq, 0, ms)
    samples = np.asarray(list(samples))
    t = ms_axis(0, len(samples))

    ax.plot(t, reference_sine(freq, 0, len(samples)), color="0.75", lw=3, label="reference")
    ax.plot(t, samples, lw=1, label="sin_tick")
    ax.set_title(f"{freq:g} Hz, one {ms} ms block")
    ax.set_xlabel("time (ms)")
    ax.set_ylim(-1.2, 1.2)
    ax.legend(loc="upper right")


def plot_two_blocks(ax, freq: float, ms: int) -> None:
    """Two back-to-back calls, so a jump at the seam stands out."""
    first, next_tick = sin_tick(freq, 0, ms)
    second, _ = sin_tick(freq, next_tick, ms)
    first = np.asarray(list(first))
    second = np.asarray(list(second))
    total = len(first) + len(second)

    ax.plot(ms_axis(0, total), reference_sine(freq, 0, total), color="0.75", lw=3, label="reference")
    ax.plot(ms_axis(0, len(first)), first, lw=1, label="block 1")
    ax.plot(ms_axis(len(first), len(second)), second, lw=1, label="block 2")
    ax.axvline(ms, color="red", ls=":", lw=1)
    ax.set_title(f"{freq:g} Hz, two {ms} ms blocks (seam at red line)")
    ax.set_xlabel("time (ms)")
    ax.set_ylim(-1.2, 1.2)
    ax.legend(loc="upper right")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--freq", type=float, nargs="+", default=[40.0], help="frequencies in Hz")
    parser.add_argument("--ms", type=int, default=50, help="block length in ms")
    parser.add_argument("--save", metavar="PATH", help="save to a file instead of opening a window")
    args = parser.parse_args()

    fig, axes = plt.subplots(len(args.freq), 2, figsize=(13, 3.2 * len(args.freq)), squeeze=False)
    for row, freq in zip(axes, args.freq):
        plot_one_block(row[0], freq, args.ms)
        plot_two_blocks(row[1], freq, args.ms)
    fig.tight_layout()

    if args.save:
        fig.savefig(args.save, dpi=120)
        print(f"saved {args.save}")
    else:
        plt.show()


if __name__ == "__main__":
    main()
