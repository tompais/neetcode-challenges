class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        i = 0
        j = 0
        seen = set()
        sl = len(s)

        while j < sl:
            if s[j] not in seen:
                seen.add(s[j])
                longest = max(longest, j - i + 1)
                j += 1
            else:
                seen.remove(s[i])
                i += 1

        return longest