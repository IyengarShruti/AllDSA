# \U0001f4a1 Approach:
# - Har character 'a' se 'z' tak check karo ki wo string me 2 baar ya zyada aata hai ya nahi.
# - Agar aata hai, to uske pehle aur aakhri occurrence ke beech wale characters check karo.
# - Beech ke unique characters count karo — yahi center hote hain palindromic subsequences ke.
# - Har outer char ke liye (jiske left aur right same character hai), unique middle characters ko count karke result me add karo.

# ⏱️ Time Complexity: O(26 * n) = O(n), kyunki 26 characters fix hain aur har ek ke liye linear scan karte hain.
# \U0001f9e0 Space Complexity: O(1), kyunki hum sirf ek set bana rahe hain har outer character ke liye (max size 26).

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0  
        for i in range(26):  # \U0001f524 Har character 'a' se 'z' tak check karenge.
            c = chr(ord('a') + i)  # \U0001f9e0 ASCII se character banaya — 'a'+0 = 'a',..., 'a'+25 = 'z'
            l, r = s.find(c), s.rfind(c)  # \U0001f50d Pehla (left) aur aakhri (right) index dhoondo

            if l == -1 or l == r:  # \U0001f615 Agar character hi nahi mila ya ek hi baar mila to skip karo
                continue

            mids = set()  # \U0001f6d1 Beech ke characters ka set — unique hi chahiye bhai!

            for j in range(l + 1, r):  # \U0001f440 Left aur right ke beech loop
                mids.add(s[j])  # \U0001f9e9 Middle characters ko set me daaldo

            res += len(mids)  # ➕ Kitne unique middle characters mile — wahi valid palindromes banayenge

        return res  
