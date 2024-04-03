# name 1: Daniel Ma
# name 2: Tyler Stratton
# name 3:

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy
from textblob import TextBlob
import math

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
                self.data.append([float(item) for item in line.split()]) # Add a given row of data into the data list
                
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
            return lm
        pass

    def evalQuality(self, line:list):
            # Given a list of scores
            # return a quality rating
            if float(line[0]) < 0.4:
                return -1 # Low Quality
            elif float(line[0]) < 0.7:
                return 0 # Medium Quality
            else:
                return 1 # High Quality

    def Quality_LR(self, sentence, LRmodel):
        # please implement this function to classify the sentence into three different classes: high, low, and medium quality
        # Input: sentence
        # output: -1 means low quality, 0 means medium quality, 1 means high quality
        # notes: you can reuse the code from the class about LR, and you can add more functions in this class as needed
        sen = self.sentenceScores(sentence)
        y_pred = LRmodel.predict(numpy.array([sen]))


        return self.evalQuality(y_pred)
        pass

    def sentenceScores(self, sentence):
        obj = sentenceQuality()
        sen = obj.calculateScores(sentence)
        return sen

class sentenceQuality():
        def __init__(self):
            # do some initialization, optional
            pass

        def calculateScores(self, tweet):
            # please implement this function
            # input: any tweet text
            # output: a list of scores for the tweet, it must include: score for length, score for Polarity, score for Subjectivity, and at least one score of the following:
            # https://en.wikipedia.org/wiki/Automated_readability_index
            # https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
            # https://en.wikipedia.org/wiki/Gunning_fog_index
            # https://en.wikipedia.org/wiki/SMOG
            # https://en.wikipedia.org/wiki/Fry_readability_formula
            # https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index
            # You should implement at least one score

            tweet = TextBlob(tweet)

            # Length
            # come back to this
            wordLength = len(tweet.words)
            length = 1.0
            if wordLength > 11 and wordLength < 16:
                length = 1.0
            else:
                if wordLength > 15:
                    num = 2
                    inc = 5
                    length = length - 0.25
                    while (wordLength >= 15 + (inc * num)):
                        num = num + 1
                        length = length - 0.25
                        if (length < 0.0):
                            length = 0.0
                elif wordLength < 12:
                    num = 2
                    inc = 4
                    length = length - 0.25
                    while (wordLength <= 12 - (inc * num)):
                        num = num + 1
                        length = length - 0.25
                        if (length < 0.0):
                            length = 0.0

            # Polarity
            polarity = tweet.sentiment.polarity

            # Subjectivity
            subjectivity = tweet.sentiment.subjectivity

            # Readability - we are using the Automated Readability Index
            minScore = 1
            maxDiff = 13
            numWords = len(tweet.words) - 1
            numChars = sum(1 for char in tweet if char.isalnum())
            numSentences = len(tweet.sentences)
            readability = math.ceil((4.71 * (numChars / numWords)) + (0.5 * (numWords / numSentences)) - 21.43)
            readability = round((readability - minScore) / maxDiff, 2) # calculated from a method to normalize scores


            return [length, polarity, subjectivity, readability]
            pass





# this is for testing only
obj = LRsentenceQuality()
s = "DATA 233 is an amazing class, and I'm going to be taking this professor's class again."
model = None
model = obj.trainLR("trainWord.txt", model)

print("The final quality for your input using LR is " + str(obj.Quality_LR(s, model)))

with open('testWord.txt', 'r') as file:
    foo = []
    for line in file:
        foo.append([float(item) for item in line.split()])
    #print(foo)
    for scores in foo:
        print("The final estimated quality for your input using LR is " + str(model.predict(numpy.array([scores[1:]]))) + ", and the actual is " + str(scores[0]))