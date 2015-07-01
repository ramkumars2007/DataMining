import csv
import os
from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
import nltk
from nltk.corpus import stopwords


# Global variables that store details about each chat transcript
chatlines = []
content_list = []
unigrams = {}

# Function to convert a file to array of chat dialogues.
def filetolist(filename):
    global chatlines;
    with open(filename) as f:
        data = f.readlines()
    for n, line in enumerate(data,1):
        chattranscripts = line.rstrip()
        chatlines.append(chattranscripts)

def listtodataset(log_id,listname):
    global content_list
    dayofchat = 1
    for i in range(0,len(chatlines)):
        charstring = ''.join(chatlines[i])
        ind_firstbreak  = charstring.find('(',0)
        ind_secondbreak  = charstring.find(' ',ind_firstbreak)
        ind_thirdbreak  = charstring.find(')',ind_secondbreak)
        user = charstring[0:ind_firstbreak].rstrip()
        datechat = charstring[ind_firstbreak+1:ind_secondbreak].rstrip()
        timechat = charstring[ind_secondbreak:ind_thirdbreak].rstrip()
        content = charstring[ind_thirdbreak+2:len(charstring)].rstrip()
        content_list.append(content)
        if i == 0:
            predator = user
            previousdate=datechat
        if previousdate <> datechat:
            dayofchat = dayofchat +1
        if user == predator:
            writeto_predatordataset(log_id,i,dayofchat,user,datechat,timechat,content)
        else:
            writeto_victimdataset(log_id,i,dayofchat,user,datechat,timechat,content)
        previousdate=datechat
        
def writeto_predatordataset(log_id,i,dayid,username,dateofchat, timeofchat, content):
    myfile = open('C:\Users\Ram\Google Drive\Statistics\Graduation - BusinessAnalytics\Spring 2015\Capstone Project\Project\Dataset\dataset_predator.csv', 'a')
    write_content_list = [i,username,dateofchat,timeofchat,content]
    myfile.write("\n"+`log_id`+'|'+`i+1`+'|'+`dayid`+'|'+username+'|'+dateofchat+'|'+timeofchat+'|'+content+'|')
    myfile.close()

def writeto_victimdataset(log_id,i,dayid,username,dateofchat, timeofchat, content):
    myfile = open('C:\Users\Ram\Google Drive\Statistics\Graduation - BusinessAnalytics\Spring 2015\Capstone Project\Project\Dataset\dataset_victim.csv', 'a')
    write_content_list = [i,username,dateofchat,timeofchat,content]
    myfile.write("\n"+`log_id`+'|'+`i+1`+'|'+`dayid`+'|'+username+'|'+dateofchat+'|'+timeofchat+'|'+content+'|')
    myfile.close()
    
def get_filepaths(directory):
    filename_list = []  
    for root, directories, files in os.walk(directory):
        for i in files:
            filename = os.path.join(root, i)
            filename_list.append(filename)  
    return filename_list  

def tokenization(contents):
    global unigrams
    for i in range(0,len(contents)):
        stop_words = stopwords.words('english')
        tokens = nltk.word_tokenize(contents[i])
        tokens = [w.lower() for w in tokens if w.lower() not in stop_words]
        


        for word in tokens:
            if word in unigrams:
                unigrams[word] += 1
            else:
                unigrams[word] = 1
    return

def print_unigrams():
    global unigrams
    output_file = open('C:/Users/Ram/Google Drive/Statistics/Graduation - BusinessAnalytics/Spring 2015/Capstone Project/Project/Dataset/unigrams.txt','w')
    for unigram in unigrams:
        count = unigrams[unigram]
        output_file.write(str(count)+'\t'+unigram+'\n')
    output_file.close()

#Main Function that calls the other functions.
def main():
    global chatlines
    global content_list
    filename_list = get_filepaths("C:/Users/Ram/Google Drive/Statistics/Graduation - BusinessAnalytics/Spring 2015/Capstone Project/Project/logs/Set 2")
    for i in range(0,len(filename_list)):
        chatlines=[]
        filetolist(filename_list[i])
        listtodataset(i+1,chatlines)
        tokenization(content_list)
        print_unigrams()
main();

