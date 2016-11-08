# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
print("""No output necessary although you can print out a success/failure message if you want to.""")
import tweepy
from textblob import TextBlob

auth = tweepy.OAuthHandler("gvCmOm8i5osgs3pG1dcQD0sFT", "rVIj4n0UBqzWg7HwfmYhNZpcCKGpTbFJletZTIZFXxqy2jJhav")
auth.set_access_token("277831482-xECfpYtnXu2ynTY4CLHDg81UDVIyaYKvmM3oZkEc", "HV4xPevmVgMOthRPLDEeLSfyTmCgSucaPyH1TYKdZaEPb")

api = tweepy.API(auth)
public_tweets = api.search('UMSI')
subjectivity = 0
polarity = 0
count = 0

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	subjectivity += analysis.sentiment.subjectivity
	polarity += analysis.sentiment.polarity
	count += 1

avg_subjectivity = subjectivity / count	
avg_polarity = polarity / count

print("Average subjectivity is " + str(avg_subjectivity))
print("Average polarity is " + str(avg_polarity))
