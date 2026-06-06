from collections import deque


class User:
    def __init__(self, id):
        self.userId = id
        self.followers = set()
        self.followees = set()


class Tweet:
    def __init__(self, id, userId):
        self.tweetId = id
        self.owner = userId


class Twitter:
    def __init__(self):
        self.users = {}
        self.tweets = deque()

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = Tweet(tweetId, userId)
        self.tweets.appendleft(tweet)

        # create new user and add tweet in their feed
        if userId not in self.users:
            self.users[userId] = User(userId)

    def getNewsFeed(self, userId: int) -> list[int]:
        # get atmost 10 tweets
        user = self.users.get(userId)
        if not user:
            return []
        feed = []
        size = 10

        if len(self.tweets) <= size:
            for tweet in self.tweets:
                if tweet.owner == userId or tweet.owner in user.followees:
                    feed.append(tweet.tweetId)
            return feed

        # fetch latest 10 feeds (queue (FIFO))
        for i in range(len(self.tweets)):
            # get tweets of himself and followees
            if self.tweets[i].owner == userId or self.tweets[i].owner \
                    in user.followees:
                feed.append(self.tweets[i].tweetId)

            if len(feed) == size:
                break

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        follower = self.users.get(followerId)
        followee = self.users.get(followeeId)
        # create follower or followee if not exist
        if follower is None:
            follower = User(followerId)
            self.users[followerId] = follower
        if followee is None:
            followee = User(followeeId)
            self.users[followeeId] = followee

        followee.followers.add(followerId)
        follower.followees.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        follower = self.users.get(followerId)
        followee = self.users.get(followeeId)

        if follower is None or followee is None:
            return

        follower.followees.discard(followeeId)
        followee.followers.discard(followerId)


obj = Twitter()
obj.postTweet(1, 5)
print(obj.getNewsFeed(1))
obj.follow(1, 2)
obj.postTweet(2, 6)
obj.postTweet(2, 1)
obj.postTweet(2, 3)
obj.postTweet(2, 3)
obj.postTweet(2, 3)
obj.postTweet(2, 3)
obj.postTweet(2, 3)
obj.postTweet(2, 3)
obj.postTweet(2, 3)
obj.postTweet(2, 3)
obj.postTweet(2, 3)
obj.postTweet(2, 3)
obj.getNewsFeed(1)
obj.unfollow(1, 2)
print(obj.getNewsFeed(2))
