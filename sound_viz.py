import numpy as np
import struct
import pyaudio
import matplotlib.pyplot as plt
from matplotlib.mlab import specgram
from scipy.io import wavfile
from IPython.display import Audio, display
from playsound import playsound
from scipy.fftpack import fft
import time
import IPython

CHUNK = 1024 * 4#How many audio sample to be processed at a time
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE =44100

p  =pyaudio.PyAudio()

stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = CHUNK

)
fig ,(ax,ax2) = plt.subplots(2 ,figsize = (15,8))
x =np.arange(0,2*CHUNK,2)
x_fft = np.linspace(0,RATE,CHUNK)
line, = ax.plot(x,np.random.rand(CHUNK))
line_fft, = ax2.semilogx(x_fft,np.random.rand(CHUNK))
ax.set_ylim(-2**15,2**15)
ax2.set_xlim(20,RATE/2)
ax.set_xlim(0,CHUNK)
ax.set_title("AUDIO WAVE")
ax2.set_title("FREQUENCY")
while(True):
    data = stream.read(CHUNK)
    data_int = struct.unpack(str(CHUNK)+'h',data)
    y_fft = fft(data_int)
    line_fft.set_ydata(np.abs(y_fft[0:CHUNK])*2 /(CHUNK*(2**14)))
    line.set_ydata(data_int)
    fig.canvas.draw()
    fig.canvas.flush_events()    