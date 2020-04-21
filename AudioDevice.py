import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write

class AudioDevice:
    sampleRate = 48000
    channels = 1

    def record(self):
        seconds = 2

        recording = sd.rec(int(seconds * self.sampleRate),
                           samplerate = self.sampleRate, channels = self.channels)
        print('Recording...')
        sd.wait()
        write('SampleLibrary/sample.wav', self.sampleRate, recording)

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

        while(1 > menuOption or 6 < menuOption):
            print("\nSampling Menu:\n")
            print("1 - Start recording")
            print("2 - Preview sample")
            print("3 - Save sample")
            print("4 - Discard sample")
            print("5 - Play sample with MIDI device")

            menuOption = int(input("\nEnter menu option here: "))
            if(1 > menuOption or 6 < menuOption):
                print("\n***Option out of range***")

        return menuOption