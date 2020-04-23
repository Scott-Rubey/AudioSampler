import os

class sampLib():
    def dispSamples(self):
        path = '/Users/srubey/PycharmProjects/CS510Sound/Project/SampleLibrary/'
        files = []
        count = 1

        for r, d, f in os.walk(path):
            for file in f:
                if '.wav' in file:
                    files.append(file)

        for f in files:
            print(count,':', f)
            count += 1
