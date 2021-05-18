#Needs relevant inputs for main.py
import driverTool

elontweets = []

elontweet = driverTool.searchTweets('username','password','elonmusk')
ifinlistelon = elontweets.count(elontweet)

if ifinlistelon == 0:
    elontweets.append(elontweet)
else:
    pass

print(elontweets)

jakepaultweets = []
jakepaultweet = driverTool.searchTweets('username','password','jakepaul')
ifinlistjakepaul = jakepaultweets.count(jakepaultweet)

if ifinlistjakepaul == 0:
    jakepaultweets.append(jakepaultweet)
else:
    pass

print(jakepaultweets)

#Now Has a way of parsing various users most recent tweet, now needs certain key words
#to determine if it has anything to do with crypto.