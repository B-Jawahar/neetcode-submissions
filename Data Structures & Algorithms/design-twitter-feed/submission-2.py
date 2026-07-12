class node:
    def __init__(self,val,left=None):
        self.val=val
        self.next=left

class Twitter:

    def __init__(self):
        self.users={}
        self.head=node([0,-1])

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId]=set()
        tmp=node([userId,tweetId])
        tmp.next=self.head
        self.head=tmp

    def getNewsFeed(self, userId: int) -> List[int]:
        result=[]
        curr=self.head
        while len(result)<10 and curr:
            if curr.val[0]==userId:
                result.append(curr.val[1])
            elif curr.val[0] in self.users[userId]:
                result.append(curr.val[1])
            else:
                pass
            curr=curr.next
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId]=set()
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            return
        self.users[followerId].discard(followeeId)
