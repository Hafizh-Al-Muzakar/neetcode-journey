class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i 
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i,hashmap[complement]]
            
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([3,2,4],6))