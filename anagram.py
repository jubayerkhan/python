class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        def character_count(cher):
            counts = {}
            for i in cher:
                if i in counts:
                    counts[i] += 1
                else:
                    counts[i] = 1
            return counts
        return character_count(s) == character_count(t)
    
solution = Solution()

print(solution.isAnagram("anagram", "nagaram"))