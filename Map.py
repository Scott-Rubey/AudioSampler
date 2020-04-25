class Map():
    startNote = None
    startFreq = None
    midiA = 69
    midiLow = 21
    midiHigh = 108

    def __init__(self, startNote):
        #difference between input note and A440, which maps to 69 on a MIDI keyboard
        noteDiff = startNote - self.midiA
        startFreq = 440 * (2**(noteDiff / 12))

        #sanity check
        print("The starting frequency is: ", startFreq)

