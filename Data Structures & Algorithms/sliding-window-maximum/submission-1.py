class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() #storing indices
        res = []
        left = 0
        for right in range(len(nums)):
            #remove elements smaller than nums[right]
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            q.append(right)
            # Remove leftmost element if it's outside the window
            if q[0] < right - k + 1:
                q.popleft()

            #Once we have a full window, record the max
            if right >= k - 1:
                res.append(nums[q[0]])
            
        return res