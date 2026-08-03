# import nltk

# # Download the 'punkt_tab' resource
# nltk.download('punkt_tab')

# from nltk.tokenize import word_tokenize

# text = 'We are learning NLP. I am excited about it.'
# tokens = word_tokenize(text)
# print(tokens)

# span = tokens[1:7]
# print(span)

# Exercise 1

import nltk
import spacy

nlp = spacy.load('en_core_web_sm')

nltk.download('punkt_tab', 'stopwords')
from nltk.tokenize import word_tokenize, sent_tokenize

text = 'Why, sometimes I`ve believed as many as 6 impossible things before breakfast? One apple a day' 
tokens = word_tokenize(text)
print(tokens)
sentences = sent_tokenize(text)
print(sentences)



from nltk.corpus import stopwords
print(stopwords.words('english'))
