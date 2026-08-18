class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}

        for i in range(len(nums)):
            a[nums[i]] = i
        
        i = 0
        for num in nums:
            diff = target - num

            if diff in a and a[diff] != i:
                return [i,a[diff]]
            i += 1
        
        
        
        