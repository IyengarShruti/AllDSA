class Solution:
    # Approach: Bigger to smallest : add
    # But if smaller to larger: sub
    # TC:O(n) and SC: O(n) for hashmap 
    def romanToInt(self, s: str) -> int:

        roman = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        }
        
        res = 0
        for i in range(len(s)):
            if i+1 < len(s) and roman[s[i]]<roman[s[i+1]]:
                # chote se bada 
                res -= roman[s[i]]
            else:
                # bade se chota
                res += roman[s[i]]
        return res
