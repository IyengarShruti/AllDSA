class Solution:
    # Approach: use map, backtrack karo charcater add kar karke
    # TC: O(n*4^n) because max 9 wala 4 characters le raha hai
    # SC: O(n) map ke karan
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        # map karo har digit ko uske letter combi ke saath
        digitsToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }    
        def backtrack(i, curStr):
            # Agar string jo bana rahe hai woh digits ke length ta hogaya 
            # jaise ki 23 -> ab, toh add karo res mein
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            # eg: 23-> i = 0 -> 2-> digitsToChar[2] -> abc
            for c in digitsToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        # call this function, start karo 0th index se and empty string
        if digits:
            backtrack(0, "")

        return res