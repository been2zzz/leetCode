class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        answer = []
        most_common_elements = freqs.most_common(k)
        for ele in most_common_elements:
            answer.append(ele[0])
        return answer