class Solution:
#   Approach: Greedy
# TC:O(n) and SC: O(n) due to hashmap
    def findMaxLength(self, nums: List[int]) -> int:
        countZero, countOne, maxL = 0,0,0
        diff_idx = {} #countOne-countZero -> index

        for i, v in enumerate(nums):
            if v == 0:
                countZero += 1
            else:
                countOne += 1
            # put the diff in hashmap
            if countOne - countZero not in diff_idx:
                diff_idx[countOne - countZero] = i
            
            if countOne == countZero:
                maxL = countOne + countZero
            else:
                # if the diff in zeros and ones already in hashmap,
                #  find index and subtract from current index
                maxL = max(maxL, i - diff_idx[countOne - countZero])

        return maxL