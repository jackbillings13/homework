# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
import nltk 
import random

# # import nltk
# nltk.download('punkt')
from nltk.book import text2

from nltk import word_tokenize,sent_tokenize

debug = True
# print(text2)
# # get file from user to make mad lib out of
# fname = text2 # need a file with this name in directory

# f = open(fname, 'r')
# para = text2.read()

tokens = text2[:150]
for i in tokens:
	print(i, end=' ')
# print("TOKENS")
# print(tokens)
tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
# print("TAGGED TOKENS")
# print(tagged_tokens)
# if debug:
# 	print ("First few tagged tokens are:")
# 	for tup in tagged_tokens[:5]:
# 		print (tup)

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []


for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))