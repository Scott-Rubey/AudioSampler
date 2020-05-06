# MIDIdevice.py
from __future__ import print_function
import logging
import sys
import time
from rtmidi.midiutil import open_midiinput, open_midioutput

class MIDIdevice:

    def midiSetup(self):
        log = logging.getLogger('midiin_poll')
        logging.basicConfig(level=logging.DEBUG)

        # Prompts user for MIDI input port, unless a valid port number or name
        # is given as the first argument on the command line.
        # API backend defaults to ALSA on Linux.
        # print("input value: ")
        port = sys.argv[1] if len(sys.argv) > 1 else None

        try:
            midiin, port_name = open_midiinput(port)
        except (EOFError, KeyboardInterrupt):
            sys.exit()

        try:
            midiout, port_name = open_midioutput(port)
        except (EOFError, KeyboardInterrupt):
            sys.exit()

        return midiin, midiout

    def playMIDI(self, midiin, midiout):
        print("\n\nReady for midi controller input. Press Control-C to exit.")
        try:
            timer = round(time.time(), 3)
            while True:
                msg = midiin.get_message()
                if msg:
                    message, deltatime = msg
                    timer += deltatime

                    if message[2] != 0:  # sending note on event:
                        midiout.send_message(message)
                        # ### sanity check to confirm input
                        print(message, deltatime)

                    else:  # sending note off event:
                        message[0] = 128
                        midiout.send_message(message)
                        # ### sanity check to confirm input
                        print(message, deltatime)

                time.sleep(0.001)
        except KeyboardInterrupt:
            print('')
        finally:
            print("Exit.")
            midiin.close_port()
            midiout.close_port()
            del midiin
            del midiout

    def getStartNote(self, midiin, midiout):
        message = [0]
        time.sleep(4)
        msg = midiin.get_message()
        if msg:
            message, deltatime = msg
            midiout.send_message(message)

        startNote = message[1]

        #make sure we don't have a residual note-on message
        message[0] = 128
        midiout.send_message(message)

        return startNote

""" # Main for testing purposes 
if __name__ == "__main__":
    pass
    midiDevice = MIDIdevice()
    midiIn, midiOut = midiDevice.midiSetup()
    midiDevice.playMIDI(midiIn, midiOut)
"""
"""Adapted from rtmidi tutorial midiin_poll.py."""