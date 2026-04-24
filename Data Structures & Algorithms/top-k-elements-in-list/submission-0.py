class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))

        k_count = 1
        result = []
        for key, value in sorted_count.items():
            if k_count <= k:
                result.append(key)
            else:
                return result
            k_count += 1
        return result
        
        