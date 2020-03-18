from nltk.tokenize import word_tokenize, casual_tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
corpusName = "corpus.txt"
corppusTagged = "corpus_tagged.txt"

def readCorpusFromFile(corpusName):
    file = open(corpusName,'r')
    return file.read()

def tokenizeText(text):
    return casual_tokenize(text)

def fileWords():
    with open("word.txt","w+") as file1:
        for tok in listOfTokens:
            count_words = 0
            for index in listOfTokens:
                if index == tok:
                    count_words = count_words + 1
            file1.write(str(tok) + ' ' + str(count_words) + '\n')
        file1.close()

def wordFreq(word):
    count_words = 0
    for index in listOfTokens:
        if index == word:
            count_words = count_words + 1
    return count_words

def filePair():
    with open("pair.txt","w+") as file2:
        for i in range(0,len(listOfTokens)-1):
            count = 0
            word1 = listOfTokens[i]
            word2 = listOfTokens[i+1]
            for j in range(0,len(listOfTokens)-1):
                if(word1 == listOfTokens[j] and word2 == listOfTokens[j+1]):
                    count = count + 1
            file2.write(str(word1) + ' ' + str(word2)+ ' ' + str(count) + ' ' + str(wordFreq(str(word1))/count) +'\n')
        file2.close()


def getSentence( listOfSentence):
    '''Data can be split into sentences'''
    return sent_tokenize(listOfSentence)

def sentenceTagging(text):
    with open("corpus_tagged.txt", "w+") as file3:
        list = getSentence(text)
        for i in range(len(list)):
            list[i] = ''.join(('<s>', list[i], '</s>'+"\n"))
        file3.write(str(list)+'\n')
    file3.close()

text = readCorpusFromFile(corpusName).encode('utf-8')
sentenceTagging(text)
text2=readCorpusFromFile(corppusTagged)

listOfTokens = tokenizeText(text2)

distinct_count = len(set(listOfTokens))
print ("distinct_count",distinct_count)
# print(len(listOfTokens))

#Marimea vocabularului
# print(len(set(listOfTokens)))

fileWords()
filePair()
