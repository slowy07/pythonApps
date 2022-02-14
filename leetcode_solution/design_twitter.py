import collections
import heapq


class Twitter(object):

    def __init__(self):
        self.__number_of_most_recent_tweets = 10
        self.__followings = collections.defaultdict(set)
        self.__messages = collections.defaultdict(list)
        self.__time = 0
        

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.__time += 1
        self.__messages[userId].append((self.__time, tweetId))
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        max_heap = []
        if self.__messages[userId]:
            heapq.heappush(max_heap, (-self.__messages[userId][-1][0], userId, 0))
        for uid in self.__followings[userId]:
            if self.__messages[uid]:
                heapq.heappush(max_heap, (-self.__messages[uid][-1][0], uid, 0))

        result = []
        while max_heap and len(result) < self.__number_of_most_recent_tweets:
            t, uid, curr = heapq.heappop(max_heap)
            nxt = curr + 1
            if nxt != len(self.__messages[uid]):
                heapq.heappush(max_heap, (-self.__messages[uid][-(nxt+1)][0], uid, nxt))
            result.append(self.__messages[uid][-(curr+1)][1])
        return result

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId != followeeId:
            self.__followings[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.__followings[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
