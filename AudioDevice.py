import sounddevice as sd
from scipy.io.wavfile import write, read
import time
import numpy as np
import librosa

class AudioDevice:
    sampleRate = 48000
    channels = 1

    def record(self):
        '''
        def trimSamp(sample):
            samp = np.array(sample.astype(np.float32))
            scaledSamp = samp * (2 ** -15)

            # remove silence at the beginning and end of the sample
            trimmedSamp, _ = librosa.effects.trim(scaledSamp, 40)

            # rescale to int16
            rescaledSamp = trimmedSamp * (2 ** 15)
            finalSamp = np.array(rescaledSamp.astype(np.int16))

            return finalSamp
        '''

        def countdown(sec):
            while(sec > 0):
                print(sec, end = '\n')
                time.sleep(1)
                sec -= 1

        countdown(3)

        duration = 2
        audioSamp = sd.rec(int(duration * self.sampleRate), dtype = 'int16',
                           samplerate = self.sampleRate, channels = self.channels)
        print('\n***Recording***')
        sd.wait()

        #normalize the sample
        #samp = trimSamp(audioSamp)
        samp = audioSamp
        finalSamp = samp / (np.max(np.abs(samp), axis = 0) / 0.95)

        return finalSamp

    def play(self, sample):
        sd.play(sample, self.sampleRate)

    def stop(self, sample):
        sd.stop()

    def save(self, sample, filename):
        newFilename = None
        substr = '.wav'

        if filename.endswith(substr):
            newFilename = filename[:-(len(substr))]
        else:
            newFilename = filename

        fullFileName = 'SampleLibrary/' + newFilename + '.wav'
        write(fullFileName, self.sampleRate, sample)

    def load(self, filename):
        sRate, source = read('SampleLibrary/' + filename)
        return sRate, source

class Util:
    def mainMenu(self):
        menuOption = 0

        while(1 > menuOption or 3 < menuOption):
            print("\nMain Menu:\n")
            print("1 - Record Sample")
            print("2 - Sample Library")
            print("3 - Exit Program")

            menuOption = int(input("\nEnter menu option here: "))
            if(1 > menuOption or 3 < menuOption):
                print("\n***Option out of range***")

        return menuOption

    def recSampleMenu(self):
        menuOption = 0

        while(1 > menuOption or 3 < menuOption):
            print("\nSampling Menu:\n")
            print("1 - Start recording")
            print("2 - Play sample with MIDI device")
            print("3 - Return to Main Menu")

            menuOption = int(input("\nEnter menu option here: "))
            if(1 > menuOption or 3 < menuOption):
                print("\n***Option out of range***")

        return menuOption

    def newSampleMenu(self):
        menuOption = 0

        while(1 > menuOption or 3 < menuOption):
            print("\n1 - Preview sample")
            print("2 - Save sample")
            print("3 - Discard sample")

            menuOption = int(input("\nEnter menu option here: "))
            if(1 > menuOption or 3 < menuOption):
                print("\n***Option out of range***")

        return menuOption

    def sampleLibMenu(self):
        menuOption = 0

        while(1 > menuOption or 4 < menuOption):
            print("\nSample Library Menu:\n")
            print("1 - Display sample list")
            print("2 - Select sample")
            print("3 - Delete sample")
            print("4 - Return to Main Menu")

            menuOption = int(input("\nEnter menu option here: "))
            if(1 > menuOption or 4 < menuOption):
                print("\n***Option out of range***")

        return menuOption

    def selectSampleMenu(self):
        menuOption = 0

        while(1 > menuOption or 4 < menuOption):
            print("\n1 - Preview current sample")
            print("2 - Load current sample to MIDI device")
            print("3 - Delete current sample")
            print("4 - Return to previous menu")

            menuOption = int(input("\nEnter menu option here: "))
            if(1 > menuOption or 4 < menuOption):
                print("\n***Option out of range***")

        return menuOption
