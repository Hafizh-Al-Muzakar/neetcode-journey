class Solution:
    def longestConsecutive(self,nums : list[int])-> int:
        numSet = set(nums)

        longest = 0
        for n in numSet :
            if (n-1) not in numSet : # check wheter n is a start of sequence or not
                length = 1
                while (n+length) in numSet:
                    length += 1
                longest = max(length,longest)
        return longest
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([1,2,3,4,5,6,8,9,7,10,12]))