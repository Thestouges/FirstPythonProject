import re

class WordFinder:
    letters = ""
    wordLength = 0
    wordList = []
    dictionary = open("dictionary.txt","r")
    
    def __init__(self, length, letters):
        self.letters = letters
        self.wordLength = length
    
    def findworld(self):
        pattern = r"[]"
        for word in self.dictionary:
            word = word.rstrip('\n')
            if(self.wordLength == len(word)):
                self.wordList.append(word)
                for x in self.letters:
                    pattern = r"["+x+"]"
                    if not (re.search(pattern, word)):
                        del self.wordList[-1]
                        break
        self.printlist()
    
    def printlist(self):
        for x in range(len(self.wordList)):
            print(self.wordList[x])