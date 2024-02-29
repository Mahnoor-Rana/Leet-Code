class Solution:
    def romanToInt(self, s: str) -> int:
        chars = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=0
        output = 0
        while i < len(s):
            if i + 1 < len(s) and chars[s[i]] < chars[s[i+1]]:
                output = output + (chars[s[i+1]] - chars[s[i]])
                i += 2
            else:
               output +=chars[s[i]]
               i+=1
        return output
