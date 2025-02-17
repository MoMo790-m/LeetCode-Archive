class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        parentheses = {')' : '(' , ']' : '[','}' :'{'}

        for string in s :
            if string in parentheses :
                if stack and stack[-1] ==  parentheses[string]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(string)

        return True if not stack else False
