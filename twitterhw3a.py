# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy

# tokens needed to access twitter
auth = tweepy.OAuthHandler("gvCmOm8i5osgs3pG1dcQD0sFT", "rVIj4n0UBqzWg7HwfmYhNZpcCKGpTbFJletZTIZFXxqy2jJhav")
auth.set_access_token("277831482-xECfpYtnXu2ynTY4CLHDg81UDVIyaYKvmM3oZkEc", "HV4xPevmVgMOthRPLDEeLSfyTmCgSucaPyH1TYKdZaEPb")

# connects to twitter api
api = tweepy.API(auth)

# sends the tweet
api.update_with_media('homework3.jpg', '#UMSI-206 #Proj3')