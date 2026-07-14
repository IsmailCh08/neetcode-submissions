class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cur_par = ''
        for item in s:
            if item in '{[(':
                stack.append(item)
            elif item in ']})':
                if not stack:
                    return False
                cur_par = stack.pop()
                if cur_par == '(' and item != ')':
                    return False
                elif cur_par == '[' and item != ']':
                    return False
                elif cur_par == '{' and item != '}':
                    return False
        if len(stack) == 0:
            return True
        else:
            return False