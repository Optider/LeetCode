class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        count = 0
        for i in shift :
            if i[0] :
                count += i[1]
            else :
                count -= i[1]
        length = len
        if count > 0 :
            count = count % length(s)
            return s[length(s)-count:]+s[:length(s)-count]
        elif count < 0 :
            count = ( count % length(s) ) - length(s)
            count *= -1 # since count is -ve
            return s[count:] + s[:count]
        else :
            return s
        
# ALTER using single mod
class Solution:
    def stringRotation(self, s: str, rotation: List[List[int]]) -> str:
        left = 0
        for d, a in rotation:
            if d:
                left -= a
            else:
                left += a
        left %= len(s)
        return s[left:] + s[:left]
