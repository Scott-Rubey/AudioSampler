import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
import time
import numpy as np
import sys

class AudioDevice:
    sampleRate = 48000
    channels = 1

    def record(self):
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
        audioSamp = audioSamp /  np.max(np.abs(audioSamp), axis = 0)
#        write('SampleLibrary/sample.wav', self.sampleRate, audioSamp)
        return audioSamp

    def play(self, filename):
        audioSample, sRate = AudioDevice.load(self, filename)
        sd.play(audioSample, sRate)
        status = sd.wait()

    def load(self, filename):
        audioSample, sRate = sf.read(filename)
        return audioSample, sRate

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
            print("\nSample Library:\n")
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
            print("2 - Load current sample")
            print("3 - Delete current sample")
            print("4 - Return to previous menu")

            menuOption = int(input("\nEnter menu option here: "))
            if(1 > menuOption or 4 < menuOption):
                print("\n***Option out of range***")

        return menuOption
