import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize
from nltk.corpus import stopwords

## List of special characters to be removed before processing the text
special_chars_list = ["\\r", "\\n", "\\'", '"', "/", "+", "-", "$", "@", "!", "#", "&", "*", "[", "]", "{", "}", "(", ")", "|", "=", ",", "?", "<", ">", ":", ";"]

def removeSpecialChars(text):
	""" Function to remove the special characters mentioned in the above list
	Gets the raw string as such, removes the special characters with empty string and return the text"""
	for special_char in special_chars_list:
		text = text.replace(special_char,"")
	text = text.replace("."," ")
	### To remove more than one fullstops with one fullstop
	#pattern = re.compile(r"(\.)\1{1,}", re.DOTALL)
	#text = pattern.sub(r"\1", text)
	return text

def tokenize(text):
	""" Function to split the raw text into words """
	words = word_tokenize(text)
	return words

def lemmatize(words):
	""" Function to lemmatize the words. Stemming is the process of stripping off the affixes. A further step is to make sure the resulting form is a known word in the dictionary, a task known as lemmatization """
	lmtzr = WordNetLemmatizer()
	words = [lmtzr.lemmatize(w) if len(w)>3 else w for w in words]
	return words

def makeLower(words):
	""" Function to normalize the text by converting the text to lower case"""
	words = [w.lower() for w in words]
	return words

def removeStopWords(words):
	""" Function to remove the stop words """
	stop_words = stopwords.words('english')
	words = [w.lower() for w in words if w.lower() not in stop_words]
	return words

if __name__ == "__main__":
	### Reading the input file which is stored in the form of csv ###
	input_file_name = "../Data/NPS_Comments_Data_new.csv"
	input_file_handle = open(input_file_name)

	out_file_name= "Topics.csv"
	out_file_handle = open(out_file_name, "w")
	out_file_handle.write("Quality,Delivery,Package,Price,Payment,CustomerContact,UI,Return,CustomerSatisfaction,CustomerIssues\n")

	### Initalizing lists which will be used to compute frequency distribution ###
	text_corpora = []
	bi_gram_corpora = []

	### Reading the lines in text file and preprocessing it ###  
	for text in input_file_handle:
		out_list = []
		### Stripping the newline characters present if any
		text = text.strip()
		### Function call to remove special characters
		text = removeSpecialChars(text)
		### Function call to convert to lower case
		text = makeLower([text])[0]
		if "damag" in text or "qualit" in text:
			out_list.append('1')
		else:
			out_list.append('0')

		if "deliver" in text or "shipment" in text or "tracking" in text or "courier" in text or "address" in text:
			out_list.append('1')
                else:
                        out_list.append('0')

		if "pack" in text or "box" in text:
			out_list.append('1')
                else:
                        out_list.append('0')

		if "price" in text or "discount" in text:
			out_list.append('1')
                else:
                        out_list.append('0')

		if "money" in text or "cash" in text or "payment" in text or "paid" in text:
			out_list.append('1')
                else:
                        out_list.append('0')

		if "call" in text or "mail" in text or "contact" in text or ("customer" in text and "care" in text):
			out_list.append('1')
                else:
                        out_list.append('0')

		if "site" in text:
			out_list.append('1')
                else:
                        out_list.append('0')

		if "return" in text or "replace" in text or "refund" in text:
			out_list.append('1')
                else:
                        out_list.append('0')

		if "satisf" in text or "happy" in text or "awesome" in text or "excellen" in text or "nice" in text:
                        out_list.append('1')
                else:
                        out_list.append('0')

		if "bad" in text or "problem" in text:
                        out_list.append('1')
                else:
                        out_list.append('0')

		out_file_handle.write(",".join(out_list)+"\n")


	input_file_handle.close()
	out_file_handle.close()
