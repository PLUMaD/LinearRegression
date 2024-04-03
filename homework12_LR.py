# name 1: Daniel Ma
# name 2: Tyler Stratton
# name 3:

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy

class LRsentenceQuality():
    def __init__(self):
        # do some initialization, optional
        self.data = []
        self.quality = []
        self.x = []
        self.y = 0
        pass
    
    def trainLR(self, trainingData, LRmodel):
        # traing a LR model on the training dataset, your group should find a training dataset with three different qualities
        with open(trainingData, 'r') as file:
            file.readline() # skip a line for the header
            
            # Read the traingData
            for line in file:
                self.data.append([item for item in line.split()]) # Add a given row of data into the data list
                
                self.quality.append(self.evalQuality(self.data[-1])) # Take the last element of data and get the evaluation
            # Prepare a numpy array to give to knn
            # Fill the y values
            self.y = numpy.array(self.quality)
            # Fill the x values
            for line in self.data:
                temp = line[1:]
                self.x.append(temp)
            self.x = numpy.array(self.x)
            
            # Construct model
            lm=LinearRegression()
            lm.fit(self.x, self.y)
        pass

    def evalQuality(self, line:list):
            # Given a list of scores
            # return a quality rating
            if line[0] < 0.4:
                return -1 # Low Quality
            elif line[0] < 0.7:
                return 0 # Medium Quality
            else:
                return 1 # High Quality

    def Quality_LR(self, sentence, LRmodel):
        # please implement this function to classify the sentence into three different classes: high, low, and medium quality
        # Input: sentence
        # output: -1 means low quality, 0 means medium quality, 1 means high quality
        # notes: you can reuse the code from the class about LR, and you can add more functions in this class as needed

        return 0
        pass




# this is for testing only
obj = LRsentenceQuality()
s = "DATA 233 is a wonderful class!"

print("The final quality for your input using LR is " + str(obj.Quality_LR(s)))
