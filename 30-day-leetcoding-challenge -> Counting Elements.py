class Solution:
    def countElements(self, arr: List[int]) -> int:
        i, j, count = 0, 1, 0
        n = len(arr)
        arr.sort()
        
        while j<n :
            if (arr[i] + 1) == arr[j] :
                count += 1
                i += 1
                j = i + 1
            elif arr[i] == arr[j] :
                j += 1
                continue
            else :
                i = j
                j += 1
        return count
