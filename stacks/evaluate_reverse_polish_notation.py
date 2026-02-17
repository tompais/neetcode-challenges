from collections import deque
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: int(x / y)}
        stack = deque()

        for token in tokens:
            if token in operations:
                right = stack.pop()
                left = stack.pop()
                stack.append(operations[token](left, right))
            else:
                stack.append(int(token))

        return stack.pop()
