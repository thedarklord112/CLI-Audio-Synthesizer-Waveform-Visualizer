import os
import numpy as np

class WaveformVisualizer:
    def __init__(self, width: int = 80, height: int = 15):
        self.width = width
        self.height = height

    def render_waveform_frame(self, audio_data: np.ndarray):
        """
        Downsamples a chunk of the raw sound array and plots an animated
        text-based oscilloscope preview directly onto the terminal screen.
        """
        # Clear screen so frames overlay smoothly without terminal flickering scrolling issues
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("🔊 CLI WAVEFORM OSCILLOSCOPE REAL-TIME STREAM 🔊")
        print("=" * self.width)

        # Slice a small readable chunk from the audio signal array to fit the text screen width
        sample_chunk = audio_data[:self.width] if len(audio_data) >= self.width else np.resize(audio_data, self.width)
        
        # Build an empty blank canvas matrix map array filled with dot placeholders
        canvas = [[" " for _ in range(self.width)] for _ in range(self.height)]
        mid_row = self.height // 2

        for col, amplitude in enumerate(sample_chunk):
            # Map floating point values (-0.3 to 0.3 range) to integer matrix rows bounds
            normalized_amp = amplitude / 0.3  # Scale to -1.0 to 1.0 range
            row_offset = int(normalized_amp * (self.height // 2 - 1))
            target_row = mid_row - row_offset
            
            # Bound clamping safe checks
            target_row = max(0, min(self.height - 1, target_row))
            
            # Place character tracking nodes
            canvas[target_row][col] = "▣"

        # Output the formatted screen layer rows
        for row in canvas:
            print("".join(row))
            
        print("=" * self.width)
