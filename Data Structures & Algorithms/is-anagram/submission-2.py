import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False
            
        # Counter creates a hash map of character frequencies
        return collections.Counter(s) == collections.Counter(t)