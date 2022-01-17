class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if not self.min_stack or val < self.min_stack[-1][0]:
            self.min_stack.append([val,1])
        elif val== self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1][0]:
            self.min_stack[-1][1] -= 1
        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
minStack = MinStack();
minStack.push(0);
minStack.push(1);
minStack.push(0);
print(minStack.getMin())# return -3
print(minStack.pop())
print(minStack.top())    # return 0
print(minStack.getMin()) # return -2