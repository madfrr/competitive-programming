#217. Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)

    return False

