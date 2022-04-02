class Solution:
    def romanToInt(self, s: str) -> int:
        romanDic = {"": 0, 'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        resultNum = 0
        flag_skipToNext = False
        inputRomanLen = len(s)
        inputIter = iter(range(inputRomanLen))
        for i in inputIter:
            curChar = s[i]
            nextChar = ""
            if i < inputRomanLen-1:
                nextChar = s[i+1]
            curInt = romanDic[curChar]
            nextInt = romanDic[nextChar]
            
            if nextInt > curInt:
                resultNum += (nextInt - curInt)
                next(inputIter)
            else:
                resultNum += curInt
        return resultNum