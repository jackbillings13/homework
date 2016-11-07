# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")
import nltk
nltk.download()
from nltk.tokenize import sent_tokenize, word_tokenize
text = "Hello students, how are you doing today? Have you recovered from the exam?  I hope you are feeling better.  Things will be fine."

print(sent_tokenize(text)) 
print(word_tokenize(text)) 
for i in word_tokenize(text):
	print(i)

print("\n\nEND*******")
