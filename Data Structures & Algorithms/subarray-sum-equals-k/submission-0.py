class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0: 1}
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num

            if curr_sum - k in mp:
                count += mp[curr_sum - k]

            mp[curr_sum] = mp.get(curr_sum, 0) + 1

        return count