class Solution:
    def addBinary(self, a: str, b: str) -> str:
        A=int(a,2)
        B=int(b,2)
        out=bin(A+B).replace('0b',"")
        return out