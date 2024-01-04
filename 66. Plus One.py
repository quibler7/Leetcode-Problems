class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # if last digit is 9 then make it zero and add one to it 
        # else return by adding 1 to it
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1]+digits

        
        