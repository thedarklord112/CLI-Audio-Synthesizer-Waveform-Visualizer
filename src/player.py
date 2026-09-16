import sounddevice as sd
from src.generator import AudioGenerator
from src.visualizer import WaveformVisualizer

class AudioSynthPlayer:
    def __init__(self, sample_rate: int = 44100):
        self.sample_rate = sample_rate
        self.generator = AudioGenerator(sample_rate=self.sample_rate)
        self.visualizer = WaveformVisualizer()

    def play_note(self, frequency: float, duration: float, wave_type: str = "SINE"):
        """Generates the waveform matrix arrays, calls the live terminal rendering layer and plays audio."""
        if frequency <= 0:
            return

        # 1. Synthesize raw numerical wave buffer data
        raw_audio_buffer = self.generator.generate_wave(frequency, duration, wave_type)
        
        # 2. Fire frame updates straight onto the console monitor screen
        self.visualizer.render_waveform_frame(raw_audio_buffer)
        
        # 3. Stream data synchronously to audio output device drivers
        # It reads floating-point arrays block layers and plays it immediately via native speakers
        sd.play(raw_audio_buffer, self.sample_rate)
        sd.wait()  # Block process thread until the note finishes playing to keep loops synced
