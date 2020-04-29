import numpy as np
import pyrubberband as rb

class Map():
    sample = None
    sampRate = None
    startNote = None
    startFreq = None
    midiA440 = 69
    midiLow = 21
    midiHigh = 108

    def __init__(self, startNote, sample, rate):
        self.sample = sample
        self.rate = rate
        self.startNote = startNote
        self.startFreq = Map.setStartFreq(self, self.startNote)

    def setStartFreq(self, startNote):
        #difference between input note and A440, which maps to 69 on a MIDI keyboard
        noteDiff = startNote - self.midiA440
        startFreq = 440 * (2**(noteDiff / 12))

        #sanity check
        print("The starting frequency is: ", startFreq)

        return startFreq

#pitch shifter implementation used under creative commons license via
#https://github.com/Zulko/pianoputer/blob/master/pianoputer.py
#and adapted for the intended use

    #changes frequency
    def speedx(self, stretched, factor):
        """ Speeds up / slows down a sound, by some factor. """
        indices = np.round(np.arange(0, len(stretched), factor))
        indices = indices[indices < len(stretched)].astype(int)

        return stretched[indices]


    #stretches the sample at the same pitch in the time domain
    def stretch(self, factor, window_size, h):
        """ Stretches/shortens a sound, by some factor. """
        phase = np.zeros(window_size)
        hanning_window = np.hanning(window_size)
        result = np.zeros(int(len(self.sample) / factor + window_size))

        for i in np.arange(0, len(self.sample) - (window_size + h), h*factor):
            i = int(i)
            # Two potentially overlapping subarrays
            a1 = self.sample[i: i + window_size]
            a2 = self.sample[i + h: i + window_size + h]

            # The spectra of these arrays
            s1 = np.fft.fft(hanning_window * a1)
            s2 = np.fft.fft(hanning_window * a2)

            # Rephase all frequencies
            phase = (phase + np.angle(s2/s1)) % 2*np.pi

            a2_rephased = np.fft.ifft(np.abs(s2)*np.exp(1j*phase))
            i2 = int(i/factor)
            result[i2: i2 + window_size] += hanning_window*a2_rephased.real

        # normalize (16bit)
        result = ((2**(16-4)) * result/result.max())

        return result.astype('int16')


    def pitchshift(self, n, window_size=2**13, h=2**11):
        """ Changes the pitch of a sound by ``n`` semitones. """
        factor = 2**(1.0 * n / 12.0)

        stretched = Map.stretch(self, 1.0/factor, window_size, h)
        return Map.speedx(self, stretched[window_size:], factor)
#end pianoputer
