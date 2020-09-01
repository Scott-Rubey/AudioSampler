import time
import rtmidi
import mido
import keyboard

outport = mido.open_output('loopMIDI 1')
a_pressed = False

while True:
    try:
        if keyboard.is_pressed("a") and not a_pressed:
            msg = mido.Message("note_on", note=n, velocity = 100, time = 10)
            outport.send(msg)
            a_pressed = True
        elif(keyboard.is_pressed("a") == False):
            msg = mido.Message("note_off", note=n, velocity=100, time=10)
            outport.send(msg)
            a_pressed = False

    #hit ctrl-c to exit MIDI controller mode (try pressing any key and see if it works)
    except KeyboardInterrupt:
        break

#better yet...
#adapted from https://github.com/Zulko/pianoputer/blob/master/pianoputer.py
from KeyboardMap import KeyboardMap
from AudioDevice import AudioDevice

def playSound(self, sample):
    kybdRange = range(21, 108)
    pitchShftdSmpls = [KeyboardMap.pitchshift(self, n) for n in kybdRange]
    keys = kybdRange
    sounds = map(AudioDevice.play(), pitchShftdSmpls)  #problems here, perhaps
    keySound = dict(zip(keys, sounds))
    isPlaying = {k: False for k in keys}


    #trying to push samples to the speakers...pyaudio wants bytes, instead
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1, rate=48000, output=True)
    data = np.array(sample[:self.bufferSize])
    frames = sample.size
    index = 0
    test = np.array([])

    stream.start_stream()

    while True:
        try:
            pass
            #depends on what midi library is used

        while index < frames:
            try:
                stream.write(data, exception_on_underflow=True)
            except OSError as exc:
                print(exc)
                exit(1)

            index += self.bufferSize
            data = np.array(sample[:self.bufferSize])
            np.append(test, data)

            '''
            startTime = time.time()
            sampConvert = np.empty(sample.shape)
            np.append(sampConvert, sample).tobytes()
            sampleLen = len(sampConvert)

            p = pyaudio.PyAudio()
            stream = p.open(format=pyaudio.paFloat32,
                            channels=1, rate=48000, output=True)

            for i in range(0, sampleLen, self.bufferSize):
                try:
                    stream.write(
                        sample[i:min(i + self.bufferSize, sampleLen)],
                        exception_on_underflow=True
                    )
                except OSError as exc:
                    print(exc, file = sys.stderr)
                    exit(1)

            stream.stop_stream()
            stream.close()
            p.terminate()
            endTime = time.time()
            print("Play time: ", endTime - startTime)
            '''