# Exercises
# Text Analysis 
# You have been recruited by your friend, a linguistics enthusiast, to create a utility tool that can perform analysis on a given piece of text. Complete the class 'analysedText' with the following methods -

# Constructor (__init__) - This method should take the argument text, make it lower case, and remove all punctuation. Assume only the following punctuation is used: period (.), exclamation mark (!), comma (,) and question mark (?). Assign this newly formatted text to a new attribute called fmtText.
# freqAll - This method should create and return dictionary of all unique words in the text, along with the number of times they occur in the text. Each key in the dictionary should be the unique word appearing in the text and the associated value should be the number of times it occurs in the text. Create this dictionary from the fmtText attribute.
# freqOf - This method should take a word as an argument and return the number of occurrences of that word in fmtText.

import sys

class analysedText(object):

    def __init__(self, text):

        # TODO: Remove the punctuation from <text> and make it lower case.
        # punctuations = ['.', '!', ',', '?']
        x = text.replace('.', '')
        x = x.replace('!', '')
        x = x.replace(',', '')
        x = x.replace('?', '')
        x = x.lower()

        # TODO: Assign the formatted text to a new attribute called "fmtText"
        self.fmtText = x
        pass


    def freqAll(self):

        # TODO: Split the text into a list of words
        words = self.fmtText.split(' ')

        # TODO: Create a dictionary with the unique words in the text as keys
        # and the number of times they occur in the text as values
        dict = {}
        for word in words:
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] += 1
        return dict

    def freqOf(self, word):

        # TODO: return the number of occurrences of <word> in <fmtText>
        occurence = self.freqAll()[word]
        # return self.fmtText.count(word)
        return occurence


obj = analysedText(
    "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
print(obj.freqAll())
print(obj.freqOf('et'))


sampleMap = {'eirmod': 1, 'sed': 1, 'amet': 2, 'diam': 5, 'consetetur': 1, 'labore': 1,
             'tempor': 1, 'dolor': 1, 'magna': 2, 'et': 3, 'nonumy': 1, 'ipsum': 1, 'lorem': 2}


def testMsg(passed):
    if passed:
        return 'Test Passed'
    else:
        return 'Test Failed'


# below code is for testing. 'do not change' 
print("Constructor: ")
try:
    samplePassage = analysedText(
        "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
    print(testMsg(samplePassage.fmtText ==
          "lorem ipsum dolor diam amet consetetur lorem magna sed diam nonumy eirmod tempor diam et labore et diam magna et diam amet"))
except:
    print("Error detected. Recheck your function ")
print("freqAll: ")
try:
    wordMap = samplePassage.freqAll()
    print(testMsg(wordMap == sampleMap))
except:
    print("Error detected. Recheck your function ")
print("freqOf: ")
try:
    passed = True
    for word in sampleMap:
        if samplePassage.freqOf(word) != sampleMap[word]:
            print('err', word)
            passed = False
            break
    print(testMsg(passed))

except:
    print("Error detected. Recheck your function  ")
