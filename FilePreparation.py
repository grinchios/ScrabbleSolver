import string
from urllib.request import *
import re
class mainfunc():   
    #print(chr(27) + "[2J") #acts as a universal 'clear' console method
    def alphaword(self):
        _input = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #holding numeric values           
        for i in self:  #checks each character for specific letter
            try:
                val = string.ascii_lowercase.index(i)
                _input[val] += 1
            except ValueError:
                pass
        return _input
        
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
        x = urlopen("http://dictionary.reference.com/browse/"+srch+"?s=t").read()
        try:
            x = x.decode('utf-8')
        except:
            return '1'
            pass
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
                return "1"
    
    def section(self):
        try:
            self = str(self.split('.')[0])
            self = self.split(', ')[1]
            return self
        except:
            pass
    
    wordlist = open("ospd.txt","r")
    infile = open("infile.txt","w")
    
    returnWord, definition = '', ''
    i = 1
    
    for word in wordlist:  #loops till all words are checked
        returnWord = word.strip('\n')  #gets specific line from file         
        word = alphaword(returnWord)  #pass in word to sorter            
        try:
            definition = find(returnWord)  #gets definition of the particular word
        except OSError:  #excepts the enevitable HTTPError that occurs
            pass
        if definition != '1':
            infile.write(returnWord.ljust(20) + str(points(word)).ljust(5) + section(definition) + '\n')
        print(i)
        i += 1
    
    infile.close()
