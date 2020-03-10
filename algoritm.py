from nltk.tokenize import word_tokenize, casual_tokenize
corpusName = "corpus.txt"

def readCorpusFromFile(corpusName):
    file = open(corpusName,"r")
    return file.read()

def tokenizeText(text):
    return casual_tokenize(text)

def fileWords():
    with open("word.txt","w+") as file1:
        for tok in listOfTokens:
            count = 0
            for index in listOfTokens:
                if index == tok:
                    count = count + 1
            file1.write(str(tok) + ' ' + str(count) + '\n')
        file1.close()

def filePair():
    with open("pair.txt","w+") as file2:
        for i in range(0,len(listOfTokens)-1):
            count = 0
            word1 = listOfTokens[i]
            word2 = listOfTokens[i+1]
            for j in range(0,len(listOfTokens)-1):
                if(word1 == listOfTokens[j] and word2 == listOfTokens[j+1]):
                    count = count + 1
            file2.write(str(word1) + ' ' + str(word2)+ ' ' + str(count) + '\n')
        file2.close()


text = readCorpusFromFile(corpusName)
listOfTokens = tokenizeText(text)
distinct_count = len(set(listOfTokens))
# print(len(listOfTokens))

#Marimea vocabularului
# print(len(set(listOfTokens)))

# fileWords()
# flePair()
