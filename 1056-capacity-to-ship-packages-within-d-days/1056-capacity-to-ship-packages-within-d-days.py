class Solution:
    """ Approach: Binary serach as capacity has lower bound(max of array), 
    so checked higher bound-> sum of all elements. Remmber no of ships = no of days, 
    TC: O(nlogm) 
    SC:O(1)
    """
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            ships, currCap = 1, cap

            for w in weights:
                # if the capacity - uss index ka weight negative jaata hai, toh zyada ship ki zarurat hogi
                if currCap - w < 0:
                    ships += 1
                    # and jaise hi no of ships given input se zyada hoga matlab answer not possible
                    if ships > days:
                        return False
                    # warna currCap new capacity
                    currCap = cap
                currCap -= w
            # loop ke bahar bina false wala execute kiye aajata hai matlab ship kar sakta hai 
            return True

        while l<=r:
            # mid or capacity
            cap = (l+r)//2

            if canShip(cap):
                res = min(res, cap)
                # find even smaller capacity
                r = cap - 1
            else:
                # increase the window size
                l = cap + 1
        return res