class Solution:
    def calPoints(self, ops: List[str]) -> int:
        score = []
        for o in ops:
            curScore = 0
            if o == "+":
                score.append(score[-1] + score[-2])
            elif o == "D":
                score.append(score[-1] * 2)
            elif o == "C":
                score.pop(-1)
            else :
                score.append(int(o))
        return sum(score)
        