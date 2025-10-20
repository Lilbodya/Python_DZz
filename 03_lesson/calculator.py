class Calculator:

    def sum(self, a, b):
        result = a+b
        return result
    
    def sub(self, a, b):
        result = a-b
        return result
    
    def mul(self, a, b):
        result = a*b
        return result

    def div(self, a, b):
        if (b == 0):
            raise ArithmeticError("На 0 делить нельзя")

        return a/b
     
    def pow(self, a, b=2):
        return a**b 
    
    #[1,2,3,4]
    def avg(self, nums):
        if len(nums) == 0:
            return 0
        
        s = 0
        for num in nums:
            s = s + num

        l = len(nums)

        return self.div(s, l)     
    