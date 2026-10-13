class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        bucks = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucks[freq].append(num)    

        result = []
        for i in range(len(bucks)-1,0,-1):
            for num in bucks[i]:
                result.append(num)
                if len(result) == k:
                    return result    