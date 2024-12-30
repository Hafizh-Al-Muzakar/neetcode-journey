# naive solution using sort

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         hashmap = {}

#         for s in strs :
#             sortedS = "".join(sorted(s))
#             if sortedS not in hashmap:
#                 hashmap[sortedS] = []
#             hashmap[sortedS].append(s)
#         return list(hashmap.values())


# (m*n) where m is length of strs and n is avarange len of string
class Solution:
    def groupAnagrams(self,strs: list[str]) -> list[list[str]]:
        hashmap = {}
       
        for s in strs :
            countS = [0]*26 # mapping frekuensi tiap huruf dalam string untuk dijadikan key
            for c in s :
               countS[ord(c) - ord("a")] += 1
            if tuple(countS) not in hashmap : # if you don't want to chech wheter key is already in hashmap use default hashmap dictionary
                hashmap[tuple(countS)] = []  # using tuple because in python we cannot use mutable object as key
            hashmap[tuple(countS)].append(s)
        return list(hashmap.values())

       
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(solution.groupAnagrams(["b"]))