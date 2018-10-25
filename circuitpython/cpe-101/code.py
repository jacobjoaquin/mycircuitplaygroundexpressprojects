# CPE-101 Drum Machine v0.1
# By Jacob Joaquin
#
# twitter: @jacobjoaquin
# instagram: @jacobjoaquin


import audioio
import board
import digitalio
from time import monotonic as now

# Enable speaker
speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.direction = digitalio.Direction.OUTPUT
speaker_enable.value = True
audio_files = ['amen_kick_0.wav', 'amen_snare_0.wav', 'amen_hat_0.wav']

# Audio
audio = audioio.AudioOut(board.A0)

# Rest
R = -1

# Tempo
bpm = 130        # Beats per minute (approximate in this version)
resolution = 16  # Number of steps per 4/4 measure

def note_on(filename):
    if audio.playing:
        audio.stop()
        
    wave_file = open(filename, "rb")
    audio.play(audioio.WaveFile(wave_file))
    print(filename)

def wait():
    t = now();
    while now() < t + (60 / bpm * (4 / resolution)):
        pass



print('Hello, CPE-101 Drum Machine v0.1!')

# Each row of 4 equals a quarter note
pattern = [
    # Measure 1
    0, 2, 0, 2,
    1, R, 0, R,
    0, R, 2, 0,
    1, R, 2, 1,

    # Measure 2
    0, 2, 0, 2,
    1, R, 0, R,
    0, R, R, 2,
    1, 1, 2, 1
]

# Loop through drum pattern
while True:
    for sample in pattern:
        if sample != R:
            note_on(audio_files[sample])
        wait()