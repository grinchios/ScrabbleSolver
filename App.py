# Scrabble Solver
# Using official wordlist
# Created by Callum Pritchard
def mainfunc(self, first, last):
    def alphaword(self):
        _input = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #holding numeric values           
        for i in range(0, len(self)-1):  #checks each character for specific letter
            if self[i] == "a":
                _input[0] += 1
            elif self[i] == "b":
                _input[1] += 1
            elif self[i] == "c":
                _input[2] += 1
            elif self[i] == "d":
                _input[3] += 1
            elif self[i] == "e":
                _input[4] += 1
            elif self[i] == "f":
                _input[5] += 1
            elif self[i] == "g":
                _input[6] += 1
            elif self[i] == "h":
                _input[7] += 1
            elif self[i] == "i":
                _input[8] += 1
            elif self[i] == "j":
                _input[9] += 1
            elif self[i] == "k":
                _input[10] += 1
            elif self[i] == "l":
                _input[11] += 1
            elif self[i] == "m":
                _input[12] += 1
            elif self[i] == "n":
                _input[13] += 1
            elif self[i] == "o":
                _input[14] += 1
            elif self[i] == "p":
                _input[15] += 1
            elif self[i] == "q":
                _input[16] += 1
            elif self[i] == "r":
                _input[17] += 1
            elif self[i] == "s":
                _input[18] += 1
            elif self[i] == "t":
                _input[19] += 1 
            elif self[i] == "u":
                _input[20] += 1
            elif self[i] == "v":
                _input[21] += 1
            elif self[i] == "w":
                _input[22] += 1
            elif self[i] == "x":
                _input[23] += 1                            
            elif self[i] == "y":
                _input[24] += 1                            
            elif self[i] == "z":
                _input[25] += 1
                
        return _input
            
    def compare(_input, word):
        bool = True
        for i in range(0, len(word)):
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
    
    def flchecks(printlist, first, last):
        bool = False
        if first != 0:
            if printlist.find(first,0, len(first)) != -1:
                bool = True
            
        elif last != 0:
            wordpos = len(printlist) - len(last)
            if printlist.find(last, wordpos) != -1:
                bool = True
        return bool
    
    cleanfile = open("ospd.txt", "r").readlines()
    printlist, word = '', ''
    _return = ['', 0]
    _input = alphaword(self)  #pass in input to sorter

    for word in cleanfile:  #loops till all words are checked
        _return[0] = word  #gets specific line from file        
        
        if len(self) >= len(_return[0]) - 1:  #first check, if input can have enough len for word
            word = alphaword(_return[0])  #pass in word to sorter
            
            if compare(_input, word) == True:  #compare words and add to output if word in self
                _return[1] = points(word)
                
                if first != 0:
                    if flchecks(_return[0], first, last) == True:  
                        printlist = printlist + _return[0] + " " + _return[1] + "\n"
                elif last != 0:
                    if flchecks(_return[0], first, last) == True:
                        printlist = printlist + _return[0] + " " + _return[1] + "\n"
                else:
                    printlist = printlist + _return[0] + " " + _return[1] + "\n"
    
    return printlist
    
word = str(input("Enter your avaliable letters: ").lower()) + ' '  #adds ' ' so it can be sorted by alphaword()
print(mainfunc(word, 0, 0))
    
    
    
    
    
    
    
    
    
    
