class Solution:
    
    import re

    def findLensContiguousOnes(self, binary_str: str, target_len: int) -> bool:
        if re.search(f"^{'1' * target_len}0", binary_str) is not None:
            return True
        if re.search(f"0{'1' * target_len}$", binary_str) is not None:
            return True
        if re.search(f"0{'1' * target_len}0", binary_str) is not None:
            return True
        return False

    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return len(arr)
        binary_str = "0" * len(arr)
        latest_step = -1
        for i in range(len(arr)):
            idx_of_one = arr[i] - 1
            binary_str = binary_str[:idx_of_one] + '1' + binary_str[idx_of_one + 1:]
            if self.findLensContiguousOnes(binary_str, m):
                latest_step = i + 1
        return latest_step

