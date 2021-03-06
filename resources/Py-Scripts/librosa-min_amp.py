# ======================= Add OM Variables BELOW this Line ========================

audio_files = ["C:\\Users\\Neimog\\OneDrive_usp.br\\Documents\\Samples\\Ircam\\01 Flute\\tongue-ram\\Fl-tng-ram-C3-mf.aif", "C:\\Users\\Neimog\\OneDrive_usp.br\\Documents\\Samples\\Ircam\\01 Flute\\tongue-ram\\Fl-tng-ram-C#3-mf.aif", "C:\\Users\\Neimog\\OneDrive_usp.br\\Documents\\Samples\\Ircam\\01 Flute\\tongue-ram\\Fl-tng-ram-D3-mf.aif", "C:\\Users\\Neimog\\OneDrive_usp.br\\Documents\\Samples\\Ircam\\01 Flute\\tongue-ram\\Fl-tng-ram-D#3-mf.aif", "C:\\Users\\Neimog\\OneDrive_usp.br\\Documents\\Samples\\Ircam\\01 Flute\\tongue-ram\\Fl-tng-ram-E3-mf.aif", "C:\\Users\\Neimog\\OneDrive_usp.br\\Documents\\Samples\\Ircam\\01 Flute\\tongue-ram\\Fl-tng-ram-F3-mf.aif", "C:\\Users\\Neimog\\OneDrive_usp.br\\Documents\\Samples\\Ircam\\01 Flute\\tongue-ram\\Fl-tng-ram-F#3-mf.aif", "C:\\Users\\Neimog\\OneDrive_usp.br\\Documents\\Samples\\Ircam\\01 Flute\\tongue-ram\\Fl-tng-ram-G3-mf.aif", "C:\\Users\\Neimog\\OneDrive_usp.br\\Documents\\Samples\\Ircam\\01 Flute\\tongue-ram\\Fl-tng-ram-G#3-mf.aif", "C:\\Users\\Neimog\\OneDrive_usp.br\\Documents\\Samples\\Ircam\\01 Flute\\tongue-ram\\Fl-tng-ram-A3-mf.aif", "C:\\Users\\Neimog\\OneDrive_usp.br\\Documents\\Samples\\Ircam\\01 Flute\\tongue-ram\\Fl-tng-ram-B3-mf.aif", "C:\\Users\\Neimog\\OneDrive_usp.br\\Documents\\Samples\\Ircam\\01 Flute\\tongue-ram\\Fl-tng-ram-C4-mf.aif", "C:\\Users\\Neimog\\OneDrive_usp.br\\Documents\\Samples\\Ircam\\01 Flute\\tongue-ram\\Fl-tng-ram-C#4-mf.aif", "C:\\Users\\Neimog\\OneDrive_usp.br\\Documents\\Samples\\Ircam\\01 Flute\\tongue-ram\\Fl-tng-ram-D4-mf.aif", "C:\\Users\\Neimog\\OneDrive_usp.br\\Documents\\Samples\\Ircam\\01 Flute\\tongue-ram\\Fl-tng-ram-D#4-mf.aif", ]
# ======================= Add OM Variables ABOVE this Line ========================

import matplotlib.pyplot as plt
import numpy as np
import librosa
from om_py import to_om


## =================================

def amplitude_envelope(signal, frame_size, hop_length):
    """Calculate the amplitude envelope of a signal with a given frame size nad hop length."""
    amplitude_envelope = []
    # calculate amplitude envelope for each frame
    for i in range(0, len(signal), hop_length): 
        amplitude_envelope_current_frame = max(signal[i:i+frame_size]) 
        amplitude_envelope.append(amplitude_envelope_current_frame)
    return np.array(amplitude_envelope)   

def fancy_amplitude_envelope(signal, frame_size, hop_length):
    """Fancier Python code to calculate the amplitude envelope of a signal with a given frame size."""
    return np.array([max(signal[i:i+frame_size]) for i in range(0, len(signal), hop_length)])

def min_amplitude_envelope (audio_file):
    """Calculate the amplitude envelope of a signal with a given frame size nad hop length."""
    FRAME_SIZE = 256
    HOP_LENGTH = 128
    audio, sr = librosa.load(audio_file)
    sample_duration = 1 / sr
    tot_samples = len(audio)
    duration = 1 / sr * tot_samples
    ae_audio = amplitude_envelope(audio, FRAME_SIZE, HOP_LENGTH)
    frames = range(len(ae_audio))
    t = librosa.frames_to_time(frames, hop_length=HOP_LENGTH)
    ae_audio = min(ae_audio)
    return ae_audio
    
amplitudes = []

for audio_file in audio_files:
    amp_min = min_amplitude_envelope(audio_file)
    amplitudes.append(amp_min)

to_om(amplitudes)


    

