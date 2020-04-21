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
                                print("\nPreviewing sample")

                            #if user chooses to save the sample
                            elif(2 == sampleActionChoice):
                                print("\nSaving sample")

                            #if user chooses to discard the sample
                            elif(3 == sampleActionChoice):
                                print("\nDiscarding sample")

                            sampleActionChoice = menu.newSampleMenu()

                    #if user chooses to play the recorded sample with a MIDI device
                    elif(2 == samplingChoice):
                        print("\nLoading to MIDI device")

                    samplingChoice = menu.recSampleMenu()

        #if user chooses to view Sample Library options
        if(2 == choice):
            libraryChoice = menu.sampleLibMenu()

            #while user chooses not to exit the sample library menu
            while(4 != libraryChoice):

                #if user chooses to display a list of all available samples
                if(1 == libraryChoice):
                    print("\nDisplay sample names")

                #if user chooses to select a particular sample from the library
                elif(2 == libraryChoice):
                    print("\nSelect a sample from the library -- input number? input string?")

                    #once a sample is selected from the library...
                    selectedSampleChoice = menu.selectSampleMenu()

                    #while user chooses not to return to the prior menu
                    while(4 != selectedSampleChoice):

                        #if the user chooses to preview the selected sample
                        if(1 == selectedSampleChoice):
                            print("\nPreview the selected sample")

                        #if the user chooses to load the selected sample to MIDI device
                        elif(2 == selectedSampleChoice):
                            print("\nLoad the selected sample")

                        #if the user chooses to delete the selected sample
                        elif(3 == selectedSampleChoice):
                            print("\nDelete the selected sample")

                        selectedSampleChoice = menu.selectSampleMenu()

                #if user chooses to delete a particular sample
                elif(3 == libraryChoice):
                    print("\nSelect a sample to delete -- input number? input string?")

                libraryChoice = menu.sampleLibMenu()

        choice = menu.mainMenu()

main()