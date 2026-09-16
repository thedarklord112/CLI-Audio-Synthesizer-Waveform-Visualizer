import unittest
import numpy as np
from src.generator import AudioGenerator

class TestAudioSynthEngine(unittest.TestCase):
    def setUp(self):
        self.generator = AudioGenerator(sample_rate=44100)

    def test_sine_wave_buffer_constraints(self):
        """Should verify wave outputs stay within safety float boundaries and match duration lengths."""
        sample_rate = 44100
        duration = 0.5
        expected_size = int(sample_rate * duration)
        
        wave = self.generator.generate_wave(440.0, duration, wave_type="SINE")
        
        self.assertEqual(len(wave), expected_size)
        self.assertTrue(np.max(wave) <= 0.3)  # Safety dampener threshold check
        self.assertTrue(np.min(wave) >= -0.3)

if __name__ == "__main__":
    unittest.main()
