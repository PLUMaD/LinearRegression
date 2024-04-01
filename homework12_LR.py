# name 1:
# name 2:
# name 3:


class LRsentenceQuality():
    def __init__(self):
        # do some initialization, optional
        pass
    def trainLR(self, trainingData, LRmodel):
        # traing a LR model on the training dataset, your group should find a training dataset with three different qualities

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
