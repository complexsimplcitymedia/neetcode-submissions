# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        
        for i in range(len(pairs)):
            j = i - 1
            # Keep swapping the current element to the left if it's smaller than the previous element
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1
            
            # Append a copy of the current state of the array to the result list
            res.append(pairs[:])
            
        return res