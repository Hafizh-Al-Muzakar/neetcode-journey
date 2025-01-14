class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self,val : int) -> None :
        self.stack.append(val)
        val = min(val,self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    
    def pop(self) -> None :
        del self.stack[-1]
        del self.minStack[-1]
    
    def top(self) -> int :
        return self.stack[-1]

    def getMin(self) -> int :
        return self.minStack[-1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.push(1))
    print(solution.push(2))
    print(solution.push(0))
    print(solution.getMin())
    print(solution.pop())
    print(solution.top())
    print(solution.getMin())