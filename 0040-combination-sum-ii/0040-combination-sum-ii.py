class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    # Approach: Backtracking. Ek element lo and explore karo and same element exclude karo 
    # and explore karo.. res mein append karte jao jaha target se equal ho... 
    # TC: O(n*2^n)
    # SC: O(n)
        res= []
        candidates.sort()
        def dfs(i, cur, total):
            # base case, we found the target combo
            if total == target:
                # we append the copy because we are using it aage 
                res.append(cur.copy())
                return
            # case 2:invalid combo or total exceeds target
            if i == len(candidates) or total>target:
                return
            
            # include the current element , always the next i+1
            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i])
            # we start the process by excluding the element
            # for that we need to first pop the added/included element
            cur.pop()
            # include but if we have case [1,1,1,1,1] or [1,1,1,2]
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1,cur,total)
        
        # call
        dfs(0,[],0)
        return res
           