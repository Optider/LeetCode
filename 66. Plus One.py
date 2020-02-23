# Beats 99.99% of python codes in Time complexity
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s_digits = [str(i) for i in digits]
        num = int("".join(s_digits)) + 1
        return [n for n in str(num)]
