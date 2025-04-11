class Solution:
    """
    Approach:
    - Ye problem rotated sorted array pe binary search lagane wali hai.
    - Array sorted hai but rotated hai, toh humein har baar dekhna padega kaunsa half sorted hai.
    - Phir decide karo target uss half mein hai ya nahi.
    Time Complexity: O(log n)  -> Binary search use kar rahe hai
    Space Complexity: O(1)     -> Koi extra space nahi liya
    """

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            # Agar mid pe hi target mil gaya toh life sorted \U0001f60e
            if target == nums[mid]:
                return mid

            # Check karo left half sorted hai ya nahi
            if nums[l] <= nums[mid]:
                # Left half sorted hai ✔️

                # Ab dekhte hain target uss left half mein hai ya nahi
                if target >= nums[l] and target < nums[mid]:
                    # Target left half mein hi chhupa hai \U0001f63c
                    r = mid - 1
                else:
                    # Target right side gaya hoga, udhar jao \U0001f449
                    l = mid + 1
            else:
                # Right half sorted hai ✔️

                # Ab dekhte hain target uss right half mein hai ya nahi
                if target > nums[mid] and target <= nums[r]:
                    # Target right mein hai, chalo udhar! \U0001f3c3‍♂️
                    l = mid + 1
                else:
                    # Target left side gaya hoga, wapas chalo \U0001f448
                    r = mid - 1

        # Sab dekh liya, target nahi mila \U0001f614
        return -1
