class MinStack:

    def __init__(self):
        self.cont = []
        self.min_cont = []

    def push(self, val: int) -> None:
        self.cont.append(val)
        if(len(self.min_cont)==0):
            self.min_cont.append(val)
            return
        if (val<=self.min_cont[-1]):    
            self.min_cont.append(val)

    def pop(self) -> None:
        if(len(self.min_cont)!=0 and len(self.cont)!=0):
            if(self.min_cont[-1] == self.cont[-1]):
                self.min_cont.pop()
            self.cont.pop()

    def top(self) -> int:
        if(len(self.cont)!=0):
            return self.cont[-1]
        else:
            return 0

    def getMin(self) -> int:
        if(len(self.min_cont)!=0):
            return self.min_cont[-1]
        else:
            return 0
