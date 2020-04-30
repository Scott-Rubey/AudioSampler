import numpy as np

#pitch shifter implementation used under creative commons license via
#https://github.com/Zulko/pianoputer/blob/master/pianoputer.py
#and adapted for the intended use

    #changes frequency
    def pitch(self, stretched, factor):
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

    #start jupyter notebook version
    def win_taper(N, a):
        R = int(N * a / 2)
        r = np.arange(0, R) / float(R)
        win = np.r_[r, np.ones(N - 2 * R), r[::-1]]
        stride = N - R - 1
        return win, stride

    def DFT_rescale(self, f):
        """
        Utility function that pitch shift a short segment `x`.
        """
        fft = np.fft.rfft(self.sample)
        # separate even and odd lengths
        parity = (len(X) % 2 == 0)
        N = len(X) / 2 + 1 if parity else (len(X) + 1) / 2
        Y = np.zeros(N, dtype=np.complex)
        # work only in the first half of the DFT vector since input is real
        for n in range(0, N):
            # accumulate original frequency bins into rescaled bins
            ix = int(n * f)
            if ix < N:
                Y[ix] += X[n]
        # now rebuild a Hermitian-symmetric DFT
        Y = np.r_[Y, np.conj(Y[-2:0:-1])] if parity else np.r_[Y, np.conj(Y[-1:0:-1])]
        return np.real(np.fft.ifft(Y))


    def DFT_pshift(self, f, G = 30, overlap=0):
        """
        Function for pitch shifting an input signal by applying the above utility function on overlapping segments.
        """
        N = len(self.sample)
        y = np.zeros(N)
        win, stride = Map.win_taper(G, overlap)
        for n in range(0, len(self.sample) - G, stride):
            w = Map.DFT_rescale(self.sample[n:n+G] * win, f)
            y[n:n+G] += w * win
        return y
    #end jupyter notebook version
