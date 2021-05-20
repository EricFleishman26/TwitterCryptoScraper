import driverTool
import classifier
from classes import Account


accounts = []
cryptotweets = []

names = []

name_input = ''

while name_input != 'Done':
    name_input = str(input("Enter names of People to Search on Twitter: "))
    if name_input == 'Done':
        break
    else:
        names.append(name_input)

for name in names:
    accounts.append(Account(name))

for account in accounts:
    account.tweet = driverTool.searchTweets('username', 'password', account.name)

for account in accounts:
    print(account.name)
    print(account.tweet)
    print('\n')
    type = classifier.classify(account.tweet)
    if type is True:
        cryptotweets.append(account)

'''
for tweet in cryptotweets:
    print(tweet.name)
    print(tweet.tweet)
    print('\n')
'''