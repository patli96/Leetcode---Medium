class Solution:

    def maxNonDecreasingLength(self, nums1, nums2):
        """
        We use a recursive function dp(i, prev) that represents the longest non-decreasing subarray we can make starting at index i, where prev is the previous element added.

        The base case is when we reach the end of the arrays, in which case the length is 0.

        For each index i, we consider two choices:

        Take nums1[i]. This is only valid if nums1[i] >= prev, in which case we can extend the previous subarray by 1.
        Take nums2[i]. This is only valid if nums2[i] >= prev, in which case we can also extend the previous subarray by 1.
        We make the optimal choice that gives the maximum subarray length. The final result is dp(0, -inf) starting from the beginning with no previous element.
        """
        @cache
        def dp(idx: int, prev_number: int):
            # terminating condition
            if idx == len(nums1):
                return 0
            
            res = 0
            
            if not prev_number:
                res = dp(
                    idx=idx + 1, 
                    prev_number=prev_number
                )
            
            if prev_number <= nums1[idx]:
                res = max(
                    res,
                    1 + dp(
                        idx=idx + 1,
                        prev_number=nums1[idx]
                    )
                )
            
            if prev_number <= nums2[idx]:
                res = max(
                    res,
                    1 + dp(
                        idx=idx + 1,
                        prev_number=nums2[idx]
                    )
                )

            return res

        return dp(
            idx=0,
            previous_number=0
        )

