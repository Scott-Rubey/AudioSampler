from AudioDevice import AudioDevice, Util

def main():
    audio = AudioDevice()
    menu = Util()
#    audio.play('SampleLibrary/sample.wav')

    choice = menu.mainMenu()

    #while user chooses not to exit the program
    while(3 != choice):

        #if user chooses to view sample recording options
        if(1 == choice):
            samplingChoice = menu.recSampleMenu()

            #while user chooses not to exit the sample recording menu
            while(3 != samplingChoice):

                    #if user chooses to record a sample
                    if(1 == samplingChoice):
                        audio.record()
                        sampleActionChoice = menu.newSampleMenu()

                        #while user simply wants to preview their recorded sample
                        #(saving or discarding will return user to the prior menu)
                        while(1 == sampleActionChoice):

                            #if user chooses to preview the recorded sample
                            if(1 == sampleActionChoice):
                                print("Previewing sample")

                            #if user chooses to save the sample
                            elif(2 == sampleActionChoice):
                                print("Saving sample")

                            #if user chooses to discard the sample
                            elif(3 == sampleActionChoice):
                                print("Discarding sample")

                    #if user chooses to play the recorded sample with a MIDI device
                    elif(2 == samplingChoice):
                        print("Loading to MIDI device")

        #if user chooses to view Sample Library options
        if(2 == choice):
            print("Option chosen: ", choice)

        choice = menu.mainMenu()

main()