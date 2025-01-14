class Solution:
    def twoSum(self,numbers :list[int] , target : int) -> list[int]:
        l,r = 0 , len(numbers)-1

        while l < r :
            if(numbers[l] + numbers[r] < target):
                l += 1
            elif(numbers[l] + numbers[r] > target):
                r -= 1
            else:
                return [l+1,r+1]

        
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([100,200,300,500],500))
    print(solution.twoSum([50,100,200,250,450,500],500))