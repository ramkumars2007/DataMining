import csv
import os
import math
#from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
#import nltk
#from nltk.corpus import stopwords

# Global variables that store details about each chat transcript
chatlines = []
documentID = []
content_list = []
unigrams = {}
RESULT = []
wordlist = []
classlist = []
problist = []
problines = []
countlist = [] 

# Prior Probabilities of each classes

prior_predator = 0.6
prior_notpredator = 0.4

# likelihood Probabilities 

def importlikelihood(probfilename):
    global wordlist
    global classlist
    global problist
    global problines
    with open(probfilename) as f:
        data = f.readlines()
    for n, line in enumerate(data,1):
        probVallist = line.rstrip()
        problines.append(probVallist)
        
    for i in range(0,len(problines)):
        charstring = ''.join(problines[i])
        ind_firstbreak  = charstring.find(',',0)
        ind_secondbreak  = charstring.find(',',ind_firstbreak+1)
        ind_thirdbreak  = charstring.find(',',ind_secondbreak+1)
        wordlist.append(charstring[0:ind_firstbreak].rstrip())
        classlist.append(charstring[ind_firstbreak+1:ind_secondbreak].rstrip())
        problist.append(charstring[ind_secondbreak+2:len(charstring)].rstrip())

def listtodataset():
    global content_list
    global chatlines
    global documentID
    global logval
    global dateval
    counter = 1
    for i in range(0,len(chatlines)):
        charstring = ''.join(chatlines[i])
        ind_firstbreak  = charstring.find(',',0)
        ind_secondbreak  = charstring.find(',',ind_firstbreak+1)
        ind_thirdbreak  = charstring.find(',',ind_secondbreak+1)
        logID = charstring[0:ind_firstbreak].rstrip()
        dateID = charstring[ind_firstbreak+1:ind_secondbreak].rstrip()
        content = charstring[ind_secondbreak+2:len(charstring)].rstrip()
        content_list.append(content)

        if i == 0:
            prevdateID = dateID
            documentID.append(1)
        else:
            if prevdateID <> dateID:
                documentID.append(documentID[i-1] + 1)
                prevdateID = dateID
            else:
                documentID.append(documentID[i-1])
            
def filetolist(filename):
    global chatlines
    with open(filename) as f:
        data = f.readlines()
    for n, line in enumerate(data,1):
        chattranscripts = line.rstrip()
        chatlines.append(chattranscripts)
        
def countwords():
    global wordlist
    global documentID
    global content_list
    global countlist
    for k in range(1,215):
        countlist = [] 
        for i in range(0,len(wordlist)):
            wordpattern = ''.join(wordlist[i].lower())
            wordcount  = 0
            for j in range(0,len(documentID)):
                if(documentID[j] == k ):
                    content = ''.join(content_list[j].lower())
                    wordcount  = wordcount + content.count(wordpattern)
            countlist.append(math.pow(float(problist[i]),float(wordcount)))
        likelihood_predator  = 1
        likelihood_notpredator  = 1
        for i in range(0,len(countlist)):
            if (classlist[i] == 'Predator'):
               likelihood_predator  = likelihood_predator * countlist[i]
            if (classlist[i] == 'Not Predator'):
                likelihood_notpredator  = likelihood_notpredator * countlist[i]
                
        likelihood_predator = likelihood_predator * prior_predator
        likelihood_notpredator = likelihood_notpredator * prior_notpredator
        
        if (likelihood_predator >= likelihood_notpredator ):
            predictedclass = 'Predator'
        else:
            predictedclass = 'Not Predator'
            
        with open('G:/files/output.csv','a+') as f1:
            writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
            row = [k,predictedclass]
            writer.writerow(row)
        
def main():
    global chatlines
    global content_list
    global documentID
    global results
    global wordlist
    global classlist
    global problist
    filename ="G:/files/TestingDataset.csv"
    probfilename="G:/files/Likelihood_Probability.csv"
    filetolist(filename)
    listtodataset()
    importlikelihood(probfilename)
    countwords()
    
    with open('G:/files/TestingDataset_Mod.csv','w') as f1:
        writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
        for i in range(0,len(documentID)):
            row = [documentID[i],content_list[i]]
            writer.writerow(row)
main();




