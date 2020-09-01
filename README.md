This program allows the user to record an audio sample, store it in a Sample Library, and play that sample from
a MIDI keyboard/controller.  Functionality is basic at this point in time; further features will be developed as
time allows.  Please note, this program was last tested on MacOS Catalina; I have heard that it remains buggy on Linux.


How to build and run:  
The program is broken into six files: Main.py, Util.py, AudioDevice.py, MIDIdevice.py, Map.py and SampLib.py.  
Some of these files require the use of the following external Python libraries: sound device, spicy, pyrubberband,
rtmidi, rtmidi.midiutil, pygame, numpy and os.  In order to run the program, one must simply run it in their IDE of 
choice, or type python3 Main.py if running from the command line.

Program flow is as follows:  from the main menu, the user may choose to either record a new sample or explore the
Sample Library.  If the user wishes to record a new sample, they may choose “Start recording” on the following menu.
The sample recorder will count down from 3, then record for exactly 2 seconds.  One may then preview their recorded
sample, save it to the Sample Library, or discard it.  Should the user decide to save the sample, they can then either
play it with a MIDI device through the current menu, or they may choose to edit the sample using their editor of choice
(i.e. Audacity) and access it later via the Sample Library.  

Please note: the user is encouraged to load their sample into an audio editor like Audacity to trim any leading/trailing
silence and/or reduce noise.  (This functionality remains incomplete at this time.)  One must close the program while they 
are editing their sample, then re-open it once the file has been updated; they will find the file in their SampleLibrary 
folder in the working directory (if a SampleLibrary has not been created prior to running the program for the first time, 
it will be automatically created for them once they save their first sample).  Once a file has been edited, it should be 
exported back to the SampleLibrary folder in the working directory as a 32-bit float PCM .wav file.  The user may now access 
the sample in their Sample Library through the course of regular program flow.  

The Sample Library menu, as access via the Main Menu, allows the user to display their sample list, select a sample
from that list by entering its corresponding sample number, or delete a sample, also by entering its corresponding
sample number.  Should the user decide to select a sample, they may then preview that sample, load it to a MIDI
device or delete it via the current menu system.

Loading a sample to a MIDI device is simple.  First, the MIDI device must be connected and powered on.  The user
will be asked if they would like to create a virtual MIDI input port, to which they should answer ’n’.  They will then be
given a list of available MIDI input ports, to which they should answer with the corresponding number.  The same two 
questions will be asked with regard to selecting a MIDI output port; answers should remain the same.  The user will
then be prompted to play the MIDI controller key they would like their sample mapped to.  (For instance, if the sample
consists of a plucked “A” string on a guitar, the user might choose to press an “A” on their MIDI keyboard.)  

***Please Note: it will take several seconds for the sample to be mapped to each key of the MIDI controller; the user 
will be prompted once their sample is ready for playback.  Should the user decide to return to the previous menu, 
they may press Contol-C at any time.***

This concludes standard program flow.
