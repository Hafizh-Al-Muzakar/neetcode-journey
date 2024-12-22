class Solution:
    def isAnagram(self, s: str , t: str) -> bool:
        countS , countT = {} , {}

        if len(s) != len(t):
            return False
        else :
            for c in range(len(s)) :
                countS[s[c]] = countS.get(s[c], 0) + 1
                countT[t[c]] = countT.get(t[c], 0) + 1
            return countS == countT
        

            
if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))
    print(solution.isAnagram("bbcc", "ccbc"))