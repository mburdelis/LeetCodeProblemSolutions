import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        groupByFreq =  [[] for _ in range(len(nums) + 1)]
        for n, f in count.items():
            groupByFreq[f].append(n)

        result = []
        for i in range(len(groupByFreq) - 1, 0, -1):
            for n in groupByFreq[i]:
                result.append(n)
                if len(result) == k:
                    return result

        return result[:k]
    

    def topKFrequentHeap2(self, nums: list[int], k: int) -> list[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        return heapq.nlargest(k, count.keys(), key=lambda x: count[x])
    

    def topKFrequentHeap(self, nums: list[int], k: int) -> list[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        heap = [(-f, n) for n, f in count.items()]
        heapq.heapify(heap)

        result = []
        for _ in range(k):
            f, n = heapq.heappop(heap)
            result.append(n)

        return result
    

    def topKFrequentSortEverything(self, nums: list[int], k: int) -> list[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        sortedByFreq = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return [n for n, f in sortedByFreq[:k]]
    


if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([1,1,1,2,2,3], 2))
    print(solution.topKFrequent([1], 1))
    print(solution.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))
