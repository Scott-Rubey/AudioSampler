from AudioDevice import AudioDevice, Util

def main():
    audio = AudioDevice()
    menu = Util()

    choice = menu.mainMenu()

    #while user chooses not to exit the program
    while(3 != choice):

        #if user chooses to view sample recording options
        if(1 == choice):
            samplingChoice = menu.recSampleMenu()

            #while user chooses not to exit the sample recording menu
            while(3 != samplingChoice):
                sample = None

                #if user chooses to record a sample
                if(1 == samplingChoice):
                    sample = audio.record()
                    sampleActionChoice = menu.newSampleMenu()

                    #if user chooses to preview the recorded sample
                    while(1 == sampleActionChoice):
                        audio.play(sample)
                        sampleActionChoice = menu.newSampleMenu()

                    #if user chooses to save the sample
                    if(2 == sampleActionChoice):
                        filename = input("Save as: ")
                        audio.save(sample, filename)
                        print("\n***Saved***")

                    #if user chooses to discard the sample
                    elif(3 == sampleActionChoice):
                        sample = None
                        print("\n***Sample discarded***")

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