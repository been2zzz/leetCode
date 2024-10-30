class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        count = 0

        for jewel in jewels:
            count += freqs[jewel]

        return count