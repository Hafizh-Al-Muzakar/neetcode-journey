class Solution:
    def maxArea(self,heights : list[int]) -> int:
        l,r = 0,len(heights)-1
        res = 0

        while l < r :
            area = (r-l)*min(heights[l],heights[r])
            res = max(area,res)
            if (heights[l] < heights[r]):
                l += 1
            else :
                r -= 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([1,12,5,6,7,8]))