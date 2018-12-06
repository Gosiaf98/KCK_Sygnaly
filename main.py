import wave

import numpy as np
import scipy.signal as sig
from scipy.io import wavfile
import matplotlib.pyplot as plt
from matplotlib import patches
from socket import socket

wav = wave.open("train/002_M.wav", mode = 'rb')

nframes = wav.getnframes()
data = wav.readframes(nframes)
nchannels = wav.getnchannels()
sampwidth = wav.getsampwidth()

num_samples, remainder = divmod(len(data), sampwidth * nchannels)

print('test')
# 8 bit samples are stored as unsigned ints; others as signed ints.
dt_char = 'u' if sampwidth == 1 else 'i'
a = np.fromstring(data, dtype='<%s%d' % (dt_char, sampwidth))
result = a.reshape(-1, nchannels)

plt.plot(range(nframes), abs(np.fft.fft(result)), '*')

plt.show()

plt.show