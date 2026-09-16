import sys
from src.player import AudioSynthPlayer

def start_synth_keyboard():
    player = AudioSynthPlayer()
    
    # Mapping keys to actual musical frequencies (Hz) starting from Middle C (C4)
    piano_keys = {
        'a': 261.63,  # C4 (Do)
        'w': 277.18,  # C#4
        's': 293.66,  # D4 (Re)
        'e': 311.13,  # D#4
        'd': 329.63,  # E4 (Mi)
        'f': 349.23,  # F4 (Fa)
        't': 369.99,  # F#4
        'g': 392.00,  # G4 (Sol)
        'y': 415.30,  # G#4
        'h': 440.00,  # A4 (La) - Standard tuning reference note
        'u': 466.16,  # A#4
        'j': 493.88,  # B4 (Si)
        'k': 523.25,  # C5 (Do Higher Octave)
    }

    # Available sound shapes configurations
    wave_styles = {
        '1': "SINE",
        '2': "SQUARE",
        '3': "SAWTOOTH"
    }
    
    current_wave = "SINE"

    print("🎹 WELCOME TO THE INTERACTIVE CLI AUDIO SYNTHESIZER 🎹")
    print("="*65)
    print("Step 1: Choose Wave Synth Mode (Press 1, 2, or 3):")
    print("  [1] SINE (Smooth flute sound) | [2] SQUARE (Retro 8-bit NES) | [3] SAWTOOTH (Edgy Synth)")
    print("\nStep 2: Play Notes using your keyboard rows:")
    print("  [ A=Do ] [ S=Re ] [ D=Mi ] [ F=Fa ] [ G=Sol ] [ H=La ] [ J=Si ] [ K=Do ]")
    print("  (Black keys sharps are on top: W, E, T, Y, U)")
    print("\nPress [q] to turn off the machine and exit.")
    print("="*65)

    while True:
        user_command = input("\nStrike Key & Hit Enter to Play: ").strip().lower()

        if user_command == 'q':
            print("\nShutting down oscillator pipelines. System offline.")
            sys.exit(0)

        # Handle wave style updates switching
        if user_command in wave_styles:
            current_wave = wave_styles[user_command]
            print(f"🔄 Oscillator wave model altered to: [{current_wave}]")
            continue

        # Check if typed character maps to a valid musical note trigger
        if user_command in piano_keys:
            note_freq = piano_keys[user_command]
            # Play the tone for a snappy 0.4 seconds burst duration block
            player.play_note(note_freq, duration=0.4, wave_type=current_wave)
        else:
            print("⚠️ Key unmapped! Use A, S, D, F, G, H, J, K keys to play or 1, 2, 3 to switch wave engine types.")

if __name__ == "__main__":
    start_synth_keyboard()
