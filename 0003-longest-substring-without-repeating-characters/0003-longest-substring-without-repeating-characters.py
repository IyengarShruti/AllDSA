class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l=0
        res = 0
        # r pure string mein chalega
        for r in range(len(s)):
            # left se nikalte jao jab tak r ka string agar set mein already hai
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            # warna add karo set mein 
            charSet.add(s[r])
            # maximum update akro
            res = max(res, r-l+1)       
        return res