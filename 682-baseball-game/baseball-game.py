class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            else:
                if i == 'C':
                    stack.pop()
                elif i == 'D':
                    dup = 2 * stack[-1]
                    stack.append(dup)
                elif i == '+':
                    stack.append(stack[-1] + stack[-2])
        return sum(stack)

        