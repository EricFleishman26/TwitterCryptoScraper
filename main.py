from classes import Account
import driverTool

accounts = []

names = ['elonmusk', 'jakepaul', 'daveportnoy']

for name in names:
    accounts.append(Account(name))

for account in accounts:
    account.tweets.append(driverTool.searchTweets('username', 'password', account.name))

for account in accounts:
    print(account.name)
    print(account.tweets)
    print('\n')


#Now Has a way of parsing various users most recent tweet, now needs certain key words
#to determine if it has anything to do with crypto.