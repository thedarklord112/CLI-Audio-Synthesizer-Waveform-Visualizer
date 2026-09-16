import numpy as np
from typing import List

class AudioGenerator:
    def __init__(self, sample_rate: int = 44100):
        # 44100Hz is the standard studio audio quality (44,100 measurements per second)
        self.sample_rate = sample_rate

    def generate_wave(self, frequency: float, duration: float, wave_type: str = "SINE") -> np.ndarray:
        """
        Generates a continuous raw audio wave array based on trigonometric equations.
        Values are constrained between -1.0 and 1.0 (Standard Floating Point Audio).
        """
        # Create a timeline array representing every second fragment step
        t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)
        
        if wave_type.upper() == "SINE":
            # Traditional smooth trigonometry sine wave: y = sin(2 * pi * f * t)
            wave = np.sin(2 * np.pi * frequency * t)
            
        elif wave_type.upper() == "SQUARE":
            # Retro 8-bit square wave toggling aggressively between 1.0 and -1.0 using the sign function
            wave = np.sign(np.sin(2 * np.pi * frequency * t))
            
        elif wave_type.upper() == "SAWTOOTH":
            # Linear aggressive ramp wave subtracting coordinates via mod elements
            wave = 2.0 * (t * frequency - np.floor(0.5 + t * frequency))
            
        else:
            raise ValueError(f"Unknown wave type request: {wave_type}")
            
        # Multiply by a slight safety dampener coefficient (0.3) to prevent ear-damaging volume clipping
        return wave * 0.3
