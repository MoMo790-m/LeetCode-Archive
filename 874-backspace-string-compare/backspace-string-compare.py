class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_text(text):
            stack = []
            for ch in text:
                if ch != '#':
                    stack.append(ch)
                else:
                    if stack:
                        stack.pop()
            
            return stack
        
        stack1 = process_text(s)
        stack2 = process_text(t)

        return stack1 == stack2