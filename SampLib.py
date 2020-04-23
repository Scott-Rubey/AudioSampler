import os

class sampLib():
    lib = []
    path = 'SampleLibrary'

    def __init__(self):
        #build array of samples in the library
        for root, dir, files in os.walk(self.path):
            for f in files:
                self.lib.append(f)

    def dispSamples(self):
        print("\n", "\u0332".join("Sample Library"))
        for i in range(len(self.lib)):
            print(i,':', self.lib[i])

    def getFilename(self, i):
        return self.lib[i]
