class MinStack:

    def __init__(self):
        self.st=[]
        self.minst=[]

    def push(self, val: int) -> None:
        self.st.append(val)
        if self.minst:
            self.minst.append(min(val,self.minst[-1]))
        else:
            self.minst.append(val)
        pass

    def pop(self) -> None:
        n=self.st.pop()
        #if n==self.minst[-1]:
        self.minst.pop()
        pass

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minst[-1]
