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
from nltk.book import text2
from nltk import word_tokenize,sent_tokenize

# gets first 150 words
tokens = text2[:150]
# prints first 150 words
print (" ".join(tokens))

# gives us a tagged list of tuples
tagged_tokens = nltk.pos_tag(tokens) 

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective","RB":"an adverb"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1,"RB":.1}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []
# creates the madlib
for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		# asks user to input a word
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))