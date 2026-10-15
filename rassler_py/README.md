# Core Building Blocks

- Sine Oscillator | Resonance (808, etc), LFO, beating pairs
- Envelope | Shapes value over time
  - Attack
  - Decay
  - Sustain
  - Release
- Biquad Filter | one struct that's low-pass, high-pass or band-pass depending on coefficients | shapes noise and protects the output.
- Noise Generator | rumble, short click that helps kick.
- Gain and mix | combining voices
- Limiter | cap peaks smoothly
- Sequencer | trigger envelopes and create patterns.
