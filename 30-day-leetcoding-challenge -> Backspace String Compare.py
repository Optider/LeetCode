class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def check(L) :
            stack = []
            for c in L :
                if c == "#" and len(stack) > 0 :
                    stack.pop()
                elif c != "#":
                    stack.append(c)
            return stack

        return check(S) == check(T)

    
# SOLUTION 2 : returned str of srack
#         stack_S = []
#         stack_T = []
        
#         for s in S :
#             if s != "#" :
#                 stack_S.append(s)
#             elif s == "#" and len(stack_S) > 0 :
#                 stack_S.pop()
        
#         for t in T :
#             if t != "#" :
#                 stack_T.append(t)
#             elif t == "#" and len(stack_T) > 0 :
#                 stack_T.pop()
                
#         if "".join(stack_T) == "".join(stack_T) :
#             return True
#         return False
