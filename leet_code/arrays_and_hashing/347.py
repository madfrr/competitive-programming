#347. Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/description/

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_items = {}

        for n in nums:
            frequent_items[n] = frequent_items.get(n, 0) + 1

        frequency = sorted(frequent_items.values(), reverse=True)
        frequency = frequency[:k]
        k_items = []
        for key, v in frequent_items.items():
            if v in frequency:
                k_items.append(key)
            
            if len(k_items) == k:
                break
        
        return k_items


print(Solution().topKFrequent([1,1,1,2,2,3], 2))
print(Solution().topKFrequent([1], 1))
        