import os
import nltk

#to download the stop words.
nltk.download('stopwords')
nltk.download('punkt')

# to import the word_tokenize 
from nltk.tokenize import word_tokenize

# to import the set of stop words
from nltk.corpus import stopwords

#read the file from the working dirctory.
file = open(r"archive/paragraphs.txt", "r")

#store the text in the variable.
text = file.read()

#splite the sentences into list of words.
words = word_tokenize(text)
# print(words)

# list of the stop words.
stop_words = set(stopwords.words('english')) 

# Remove stopwords
filtered_words = [word for word in words if word.lower() not in stop_words]

#concatenate the non stop words
filtered_sentence = ' '.join(filtered_words)
print(filtered_sentence)

#list of non stop words fot counting the frequency of the words.
list_word = word_tokenize(filtered_sentence)


#  dictionary 
d = {}
for word in list_word :
    if word in d :
        d[word] = d[word]+1
    else : 
        d[word] = 1

print(d)


