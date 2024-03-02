class Solution:
    def isValid(self, s):
        if len(s) % 2 != 0:
            return False
        if (s[0] in [")", "}", "]"]) or (s[-1] in ["(", "{", "["]):
            return False
        if (
            s.count("(") != s.count(")")
            or s.count("{") != s.count("}")
            or s.count("[") != s.count("]")
        ):
            return False
        else:
            brackets = {")": "(", "}": "{", "]": "["}
            stack = []
            for x in s:
                if x in brackets.keys():
                    if stack[-1] != brackets[x]:
                        return False
                    if stack[-1] == brackets[x]:
                        stack.pop()
                        continue
                stack.append(x)
            return True
