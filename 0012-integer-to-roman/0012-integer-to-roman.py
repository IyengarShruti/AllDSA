class Solution:
    # Approach: greedy approach always picks the biggest possible Roman numeral at every step — exactly how humans write Roman numerals.
    # TC: O(1) as it runs through 13 roman symbols which is fixed
    # SC: O(1)  
    def intToRoman(self, num: int) -> str:
        # pehle nested lists banao usme ye special conditions bhi daalo
        sabKuchList = [
            ["I", 1], ["IV", 4], ["V", 5], ["IX", 9],
            ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
            ["C", 100], ["CD", 400], ["D", 500], ["CM", 900],
            ["M", 1000]
        ]
        res = ""
        # peeche se iterate karo kyuki biggest->smallest jaana hai
        for sym, val in reversed(sabKuchList):
            # eg: num: 1994  num:994; num= 94
            if num // val:
            #   1994 //1000=1;994//900 -> 1; 94//90->1
                count = num//val
                 # ->add M-> add CM->XC
                res += (sym * count)
                # num = 1994%1000->994; 994%900->94; 94%90->4
                num = num % val

        return res