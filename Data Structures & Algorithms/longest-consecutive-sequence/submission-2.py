class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return 0
            
        nums_set = set(nums)

        start_list = set()

        count_list = []

        for x in nums_set:
            if x - 1 not in nums_set:
                start_list.add(x)
        
        for s in start_list:
            count = 1
            while s + 1 in nums_set:
                count += 1
                s += 1
            
            count_list.append(count)
    
        return max(count_list)
        
        


        