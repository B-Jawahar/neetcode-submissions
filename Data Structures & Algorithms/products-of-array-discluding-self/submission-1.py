class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        has_zero=0
        result=[]
        for num in nums:
            if num==0 and has_zero==0:
                has_zero=1
            elif num==0 and has_zero==1:
                product=0
                break
            else:
                product*=num
        for num in nums:
            if has_zero:
                if num!=0:
                    result.append(0)
                else:
                    result.append(product)
            else:
                result.append(int(product/num))
        return result