class Solution:
    """ Approach:
    - Ye normal school-style multiplication hai (jaise hum paper pe karte hai)
    - Har digit ko doosre number ke har digit se multiply karna hai
    - Phir proper place pe (i1+i2) add karna hai
    - Carry ko agle position mein add karna hai
    - End mein leading 0 hatao aur result join karo
    Time Complexity: O(n * m)
        n = len(num1), m = len(num2) — har digit ke saath har digit multiply
    Space Complexity: O(n + m)
        max digits ho sakte hai n+m (jaise 99 x 99 = 9801 -> 4 digits)
    """
    def multiply(self, num1: str, num2: str) -> str:
        # Agar koi ek number zero hai, toh seedha "0" return karo
        if "0" in [num1, num2]:
            return "0"

        # Final result ko rakhne ke liye array banaya
        res = [0] * (len(num1) + len(num2))

        # Dono numbers ko reverse kar diya, taaki easy position manage ho jaye
        num1, num2 = num1[::-1], num2[::-1]
        # Har digit se multiply kar rahe hai (jaise school time mein karte the \U0001f604)
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                # Dono digits ko multiply kiya
                digit = int(num1[i1]) * int(num2[i2])
                
                # Ab uska sum res mein daalo — proper position pe
                res[i1 + i2] += digit

                # Carry ko agle position mein daalo
                res[i1 + i2 + 1] += res[i1 + i2] // 10

                # Current position ka digit update karo (0–9)
                res[i1 + i2] = res[i1 + i2] % 10

        # Reverse back, kyunki humne ulta bhar diya tha
        res = res[::-1]

        # Leading zeroes hatao (example: [0, 1, 2, 3] → [1, 2, 3])
        beg = 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        # Integer array ko string mein convert karo
        res = map(str, res[beg:])
        return "".join(res)
