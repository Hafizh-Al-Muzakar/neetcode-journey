# naive solution using sort (nlogn time and n space)
# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         hashmap  = {}
#         for n in nums:
#             if n in hashmap:
#                 hashmap[n] += 1
#             else:
#                 hashmap[n] = 1
        
#         sorted_items = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
#         top_k = [item[0] for item in sorted_items[:k]]
        
#         return top_k



class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int] :
        count = {}

        freq = [[] for i in range(len(nums) + 1) ]

        for n in nums :
            count[n] = 1 + count.get(n,0)
        
        for n,c in count.items():
            freq[count[n]].append(n)
        
        res = []

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if(len(res) == k) :
                    return res
        



if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([1,2,3,4,5,6,7],2))