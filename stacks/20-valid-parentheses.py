class Solution:
    def isValid(self, s : list[str]) -> bool:
        stack = []
        closeToOpen = {"}":"{",")":"(","]":"["}

        for c in s :
            if c in closeToOpen :
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else :
                    return False
            else:
                stack.append(c)

        return False if stack else True
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("}{"))