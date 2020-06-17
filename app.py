import matplotlib.pyplot as plt
from matplotlib.mlab import specgram
from scipy.io import wavfile
import numpy as np
from skimage.feature import peak_local_max

def cut_specgram(min_freq, max_freq, spec, freqs):
    spec_cut = spec[(freqs >= min_freq) & (freqs <= max_freq)]
    freqs_cut = freqs[(freqs >= min_freq) & (freqs <= max_freq)]
    Z_cut = 10.0 * np.log10(spec_cut)
    Z_cut = np.flipud(Z_cut)
    return Z_cut, freqs_cut

def show_peaks(Z, freqs, t, coord, title):
    fig = plt.figure(figsize=(10, 8), facecolor='white')
    plt.imshow(Z, cmap='viridis')
    plt.scatter(coord[:, 1], coord[:, 0])
    ax = plt.gca()
    plt.xlabel('Time bin')
    plt.ylabel('Frequency')
    plt.title(title, fontsize=18)
    plt.axis('auto')
    # ax.set_xlim([0, len(t)])
    # ax.set_ylim([len(freqs), 0])
    # ax.xaxis.set_ticklabels([])
    # ax.yaxis.set_ticklabels([])
    plt.show()

# Read the wav file (mono)

rate1, song_array1 = wavfile.read('toto.wav')
# rate2, song_array2 = wavfile.read('Daft_Punk.wav')

#song_array1 = song_array1[:, 0]

spec1, freqs1, t1 = specgram(song_array1, NFFT=4096, Fs=rate1, noverlap=2048)
# spec2, freqs2, t2 = specgram(song_array2, NFFT=4096, Fs=rate2, noverlap=2048)



min_freq = 0
max_freq = 25000

Z1, freqs1 = cut_specgram(min_freq, max_freq, spec1, freqs1)
# Z2, freqs2 = cut_specgram(min_freq, max_freq, spec2, freqs2)

coordinates1 = peak_local_max(Z1, min_distance=20, threshold_abs=20)
# coordinates2 = peak_local_max(Z2, min_distance=20, threshold_abs=20)

show_peaks(Z1, freqs1, t1, coordinates1, 'Demo')
# show_peaks(Z2, freqs2, t2, coordinates2, 'Daft Punk song')

print(coordinates1)



# Plot the signal read from wav file

plt.subplot(211)
plt.title('Spectrogram of a wav file ')
plt.plot(song_array1)
plt.xlabel('Sample')
plt.ylabel('Amplitude') 
plt.subplot(212)
plt.specgram(song_array1,Fs=rate1,cmap='viridis')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.show()
