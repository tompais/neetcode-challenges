from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '[': ']', '{': '}'}
        stack = deque()
        sl = len(s)
        i = 0
        is_valid = True

        while i < sl and is_valid:
            char = s[i]
            if char in pairs:
                stack.append(char)
            elif not stack or pairs[stack.pop()] != char:
                is_valid = False
            i += 1

        return is_valid and not stack