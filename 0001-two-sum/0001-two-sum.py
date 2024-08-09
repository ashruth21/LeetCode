class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index={}
        for i,n in enumerate(nums):
            if target-n in index:
                return [i,index[target-n]]
            index[n]=i