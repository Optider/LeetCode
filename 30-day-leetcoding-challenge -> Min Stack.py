# SOLUTION 1: Beats 2nd. This took 60 ms, while 2nd takes 824 ms !!!
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []      

    def push(self, x: int) -> None:
        if self.stack :
            self.stack.append( ( x, min(x, self.stack[-1][1] ) ) )
        else :
            self.stack.append( (x, x) )
        print(self.stack)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# SOLUTION 2
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
