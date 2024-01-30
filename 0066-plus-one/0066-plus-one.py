class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=len(digits)
        number=0
        count=0
        for i in digits:
            count+=1
            number=number+i*10**(l-count)
        new=number+1
        new=str(new)
        out=[]
        for i in new:
            out.append(int(i))
        return out
        