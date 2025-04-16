class Solution:
    # Approach: Backtracking. Ek element lo and explore karo and same element exclude karo 
    # and explore karo.. res mein append karte jao jaha target se equal ho... 
    # TC & SC: O(2^target/minimum value in candidates)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res= []

        def dfs(i, cur, total):
            # base case, we found the target combo
            if total == target:
                # we append the copy because we are using it aage 
                res.append(cur.copy())
                return
            # case 2:invalid combo or total exceeds target
            if i >= len(candidates) or total>target:
                return
            
            # include the current element
            cur.append(candidates[i])
            dfs(i, cur, total+candidates[i])
            # we start the process by excluding the element
            # for that we need to first pop the added/included element
            cur.pop()
            dfs(i+1,cur,total)
        
        # call
        dfs(0,[],0)
        return res
        