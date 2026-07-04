class TimeMap:

    def __init__(self):
        self.tm={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.tm:
            self.tm[key].append((timestamp,value))
        else:
            self.tm[key]=[(timestamp,value)]
        pass

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tm:
            return ""
        if timestamp>=self.tm[key][-1][0]:
            return self.tm[key][-1][1]
        if timestamp<self.tm[key][0][0]:
            return ""

        left,right=0,len(self.tm[key])-1
        while left<=right:
            mid=(left+right)//2
            print(left,right,mid)
            if self.tm[key][mid][0]==timestamp:
                return self.tm[key][mid][1]
            elif self.tm[key][mid][0]<timestamp:
                if self.tm[key][mid+1][0]>timestamp:
                    return self.tm[key][mid][1]
                else:
                    left=mid+1
                print("left",left)
            else:
                right=mid-1
                print("right",right)
            
        return self.tm[key][left][1]



