import matplotlib.pyplot as plot
from matplotlib.mlab import specgram
from scipy.io import wavfile

def cut_specgram(min_freq, max_freq, spec, freqs):
    spec_cut = spec[(freqs >= min_freq) & (freqs <= max_freq)]
    freqs_cut = freqs[(freqs >= min_freq) & (freqs <= max_freq)]
    Z_cut = 10.0 * np.log10(spec_cut)
    Z_cut = np.flipud(Z_cut)
    return Z_cut, freqs_cut

# Read the wav file (mono)

samplingFrequency, signalData = wavfile.read('demo.wav')

signalData = signalData[:, 0]

# Plot the signal read from wav file

plot.subplot(211)

plot.title('Spectrogram of a wav file ')
plot.plot(signalData)
plot.xlabel('Sample')
plot.ylabel('Amplitude') 

plot.subplot(212)
plot.specgram(signalData,Fs=samplingFrequency,cmap='viridis')
plot.xlabel('Time')
plot.ylabel('Frequency')
plot.show()

min_freq = 0
max_freq = 15000

Z1, freqs1 = cut_specgram(min_freq, max_freq, signalData, samplingFrequency)
plot.specgram(Z1,Fs=freqs1,cmap='viridis')
plot.xlabel('Time')
plot.ylabel('Frequency')
plot.show()