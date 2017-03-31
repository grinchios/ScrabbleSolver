import string
from urllib.request import *
import re, os

print(chr(27) + "[2J") #acts as a universal 'clear' console method
print("Input your avaliable letters, specify first and last letters")
print("by putting them in bold at the start of the input")
print("and for the ending, type them in bold at the end of the word :)")
print('')

self = input('Enter your avaliable letters: ').lower()

print('')
first = input('Enter your specified starting chars or nothing to not specify: ').lower()  #assigment of statements before code runs
last = input('Enter your specified ending chars or nothing to not specify: ').lower()

print(chr(27) + "[2J")  #blank lines for readability

def alphaword(self):
    _input = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #holding numeric values           
    for i in self:  #checks each character for specific letter
        val = string.ascii_lowercase.index(i)
        _input[val] += 1            
    return _input
        
def compare(_input, word):
    bool = True
    for i in range(0, 26):
        if _input[i] < word[i]:  #checking if the amount of i letters in input are avaliable in the selected word
            bool = False
    return bool
    
def points(self):
    points = 0
    points += (self[4] + self[0] + self[8] + self[14] + self[13] + self[17] + self[19] + self[11] + self[18] + self[20])
    points += (self[3] + self[6]) * 2
    points += (self[1]+ self[2]+ self[12]+ self[15]) * 3
    points += (self[5]+ self[7]+ self[21]+ self[22]+ self[24]) * 4
    points += (self[10]) * 5
    points += (self[9]+ self[23]) * 8
    points += (self[16]+ self[25]) * 10
    points = str(points)
    return points

def flchecks(self, first, last):
    bool = False
    if first != '0' and last != '0':  #check first and last
        pos = len(self) - len(last)
        if self.find(first, 0, len(first)) != -1 and self.find(last,pos) != -1:
            bool = True
    elif first != '0':  #checks just first
        if self.find(first, 0, len(first)) != -1:
            bool = True
    elif last != '0':  #checks just last
        pos = len(self) - len(last)
        if self.find(last,pos) != -1:
            bool = True
    return bool

def flsort():
    readTemp = open("temp.txt","r")  #reads the temp file
    readFile = readTemp.readlines()
    tempfile = open("temp.txt","w")    

    for word in readFile:  #cycles through output file to check fl letters
        actualWord = word[:20].strip(' ')        
        if flchecks(actualWord,first,last) == True:
            actualPoints = word[20:24].strip(' ')  #definitions goes under here
            define = word[25:].strip('\n')
            tempfile.write(actualWord + ' ' + actualPoints + ' ' + define + '\n')    
    tempfile.close()

def numsort():
    tempRead = open("temp.txt","r").readlines()  #read outputs from temp file
    tempfile = open("temp.txt","w")
    for i in range(0, len(tempRead)-1):  #sort by ending numbers
        for j in range(0, len(tempRead)-1):
            if int(tempRead[j][20:25].strip(' ')) > int(tempRead[j +1][20:25].strip(' ')):  #checks if the points of one are bigger than the next
                temp = tempRead[j]
                tempRead[j] = tempRead[j+1]  #the switching of values
                tempRead[j+1] = temp
    for i in range(len(tempRead)):  #re-adding the values back into the files
        tempfile.write(tempRead[i])

def find(x):
    srch = str(x)
    x = urlopen("http://dictionary.reference.com/browse/"+srch+"?s=t").read().decode('utf-8')
    items = re.findall('<meta name="description" content="'+".*$",x,re.MULTILINE)
    for x in items:
        y = x.replace('<meta name="description" content="','')
        z = y.replace(' See more."/>','')
        m = re.findall('at Dictionary.com, a free online dictionary with pronunciation,              synonyms and translation. Look it up now! "/>',z)
        if m==[]:
            if z.startswith("Get your reference question answered by Ask.com"):
                return "Word not found!"
            else:
                return z
    else:
            return "Word not found!"

def section(self):
    self = str(self.split('.')[0])
    self = self.split(', ')[1]
    return self

wordlist = open("ospd.txt","r")
tempfile = open("temp.txt","w")

returnWord, definition = '', ''
mainWord = alphaword(self)  #pass in input to sorter  

for word in wordlist:  #loops till all words are checked
    returnWord = word.strip('\n')  #gets specific line from file         

    if len(self) >= len(returnWord) - 1:  #first check, if input can have enough len for word
        word = alphaword(returnWord)  #pass in word to sorter            

        if compare(mainWord, word) == True:  #compare words and add to output if word in self
            try:
                definition = find(returnWord)  #gets definition of the particular word
            except OSError:  #excepts the enevitable HTTPError that occurs
                pass

            tempfile.write(returnWord.ljust(20) + str(points(word)).ljust(5) + section(definition) + '\n')

tempfile.close()

numsort()  #sorts words by points

if first != '0' or last != '0':  #if the first and last need to be checked
    flsort()

for i in open('temp.txt','r').readlines():
    print(i)

os.remove("temp.txt") #removes the temp file
print('Done!')