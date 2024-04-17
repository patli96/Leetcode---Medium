class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        result = []
        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            result.extend([i + [n] for i in perms])
            nums.append(n)
        return result

