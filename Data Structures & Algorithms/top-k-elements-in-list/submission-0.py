class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])

        for num in freq:
            count = freq[num]
            buckets[count].append(num)

        result = []
        j = len(buckets) - 1
        while j >= 0:
            bucket = buckets[j]

            for num in bucket:
                result.append(num)

            if len(result) == k:
                return result

            j = j - 1


        


        