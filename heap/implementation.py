# leetcode 347: top k frequent elements
from collections import Counter
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # if k == len(nums):
        #     return set(nums)
        count = Counter(nums)
        
        return heapq.nlargest(k, count.keys(), key=count.get)
    
    