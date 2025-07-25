class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i, val in enumerate(nums):
            if hash.get(val) is not None:
                return [hash.get(val), i]
            hash[target - val] = i
            
# solução O(n) com espaço O(n)