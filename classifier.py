def classify(tweet):
    tweet = tweet.lower()
    triggerphrases = ['crypto', 'bitcoin', 'dogecoin', 'doge', 'to the moon', 'giga']

    for phrase in triggerphrases:
        if phrase in tweet:
            return True
            break
    return False
