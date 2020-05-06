import librosa as lr
import pyrubberband as prb
import os

os.environ["NUMBA_DEBUG"] = str(0)
os.environ["NUMBA_WARNINGS"] = str(0)

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
        #print("The starting frequency is: ", startFreq)

        return startFreq

    def pitchshift(self, n):
        note = n - self.startNote
        return lr.effects.pitch_shift(self.sample, 48000, note)
        #return prb.pitch_shift(self.sample, 48000, note)

