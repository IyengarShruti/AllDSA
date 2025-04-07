"""
\U0001f50d Approach:
Sliding Window Technique:
- Expand the window by moving the 'right' pointer.
- Keep track of number of 0s in the window.
- If 0s exceed k, move 'left' pointer to shrink the window.
- Track the maximum valid window size.
⏱️ Time Complexity: O(n)
- Each element is visited at most twice (once by left, once by right).
\U0001f9e0 Space Complexity: O(1)
- Only constant extra space is used.
"""
class Solution:
    def longestOnes(self, nums, k):
        left, maxLength, zeroCount = 0, 0, 0

        for right in range(len(nums)):
            # Bhai agar 0 mila toh count badhao, chori pakdi gayi!
            if nums[right] == 0:
                zeroCount += 1

            # Jab 0 ka limit cross ho gaya, toh left se window chhoti karo
            while zeroCount > k:
                # Agar left par bhi 0 hai toh count ghatana padega, warna toh bekaar
                if nums[left] == 0:
                    zeroCount -= 1
                # Window chhoti karo... ghar me jagah kam pad gayi hai
                left += 1

            # Har step par dekh lo ki ab tak ka sabse bada valid window kaun sa hai
            maxLength = max(maxLength, right - left + 1)
            
        return maxLength
