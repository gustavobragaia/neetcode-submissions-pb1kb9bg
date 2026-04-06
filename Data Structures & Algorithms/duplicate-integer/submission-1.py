class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency = dict()
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        for i in frequency.values():
            if i > 1:
                return True
        return False