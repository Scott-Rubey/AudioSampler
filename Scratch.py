import numpy as np

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
