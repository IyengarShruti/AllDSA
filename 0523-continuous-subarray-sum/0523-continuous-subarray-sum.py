# Approach: Prefix sum + hashmap
# TC:O(n) and SC: O(n)
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #  Before we start to have a map...we keep remainder as 0 and indx as -1
        # matlab ye array start hone ke pehle wala vaue
        remainder = {0: -1} #remainder is map
        total=0
        
        for i, n in enumerate(nums):
            # prefix sum nikalo
            total += n
            # Yaha check kar rahe hai ki divisible hai ya nahi
            r = total % k
            # Pehle check karo ki hashmap mein already hai ya nahi
            if r not in remainder:
                # agar nahi hai toh add karo current index
                remainder[r] = i
            # nahi toh matlab r hai remainder mein and current index se pichle index ka length 1 se zyada hai 
            # toh solution mil gaya na 
            elif i-remainder[r]>1:
                return True      
        return False

