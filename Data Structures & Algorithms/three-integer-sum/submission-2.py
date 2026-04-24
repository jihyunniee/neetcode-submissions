class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for n in range(len(nums)):
            left = n + 1
            right = len(nums) - 1

            while left < right:
                res = nums[left] + nums[right]
                if res > -(nums[n]):
                    right -= 1
                else:
                    if(res == -(nums[n])):
                        triplets.append([nums[n], nums[left], nums[right]])
                    left += 1
        
        return [list(x) for x in set(map(tuple, triplets))]
    
    
    
    