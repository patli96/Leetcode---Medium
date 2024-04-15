class Solution:
    
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zeros_in_nums1 = nums1.count(0)
        zeros_in_nums2 = nums2.count(0)
        
        if zeros_in_nums1 == 0 and zeros_in_nums2 == 0:
            if sum(nums1) != sum(nums2):
                return -1
            return sum(nums1)
        elif zeros_in_nums1 == 0 or zeros_in_nums2 == 0:
            arr_without_zero = nums1 if zeros_in_nums1 == 0 else nums2
            arr_with_zero = nums1 if zeros_in_nums1 != 0 else nums2
            if sum(arr_with_zero) >= sum(arr_without_zero):
                return -1
            if abs(sum(arr_without_zero) - sum(arr_with_zero)) / arr_with_zero.count(0) < 1:
                return -1
        
        return max(sum(nums1) + zeros_in_nums1, sum(nums2) + zeros_in_nums2)
