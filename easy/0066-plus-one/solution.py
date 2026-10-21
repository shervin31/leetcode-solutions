class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s = "".join(str(n) for n in digits)
        d = int(s)
        d += 1
        s = str(d)
        final = []
        for num in s:
            final.append(int(num))

        return final