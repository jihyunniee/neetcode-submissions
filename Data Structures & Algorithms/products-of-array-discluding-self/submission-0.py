class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i, num in enumerate(nums):
            product_array = []
            product = 1
            x = 0
            while x < len(nums):
                if x != i:
                    product_array.append(nums[x])
                
                x += 1

            for p in product_array:
                product *= p
            
            output.append(product)
        
        return output