# name 1: Daniel Ma
# name 2: Tyler Stratton
# name 3:

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class LRsentenceQuality():
    def __init__(self):
        # do some initialization, optional
        self.data = []
        self.x_train = 0
        pass
    
    def trainLR(self, trainingData, LRmodel):
        # traing a LR model on the training dataset, your group should find a training dataset with three different qualities
        with open(trainingData, 'r') as file:
            file.readline() # skip a line for the header
            
            # Read the traingData
            for line in file:
                self.data.append([item for item in line.split()]) # Add a given row of data into the data list
            # Construct model
            lm=LinearRegression()
            lm.fit(X_train, y_train)
        pass

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
