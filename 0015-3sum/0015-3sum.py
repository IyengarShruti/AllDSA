class Solution:
    # Approach: sort and use two pointer use Two pointer II 
    # TC: O(nlogn)+ two loops -> one for first value and second for solving two other values O(n^2)=>     Overall O(n^2)
    # SC: O(1) or O(n) depending on the sorting algorithm
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # matlab same value hai toh aage chalte badho bhaiya
            if i>0 and a == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            # Use two pointer to find a, b, c
            while l<r:
                threeSum = a+nums[l]+nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum<0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    # next num le lo
                    l+=1
                    # wapis same hai pichle se toh l ko aage karo
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res

        