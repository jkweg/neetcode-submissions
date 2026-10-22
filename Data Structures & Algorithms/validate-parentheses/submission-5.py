class Solution:
    def isValid(self, s: str) -> bool:

        # if len(s) % 2 != 0:
        #     return False

        seen = []
        for char in s:
            if char in ['{' , '[' , '(']:
                seen.append(char)
            else:

                if not seen:
                    return False

                if char == '}':
                    last = seen.pop()
                    if last != '{':
                        return False
                if char == ')':
                    last = seen.pop()
                    if last != '(':
                        return False
                if char == ']':
                    last = seen.pop()
                    if last != '[':
                        return False
        
        return len(seen) == 0