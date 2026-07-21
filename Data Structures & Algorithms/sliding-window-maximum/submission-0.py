class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        Max = []
        for i in range(len(nums) - k + 1):
            Max.append(max(nums[i: i+k]))
        return Max