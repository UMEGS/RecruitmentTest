from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums1_len, nums2_len = len(nums1), len(nums2)

        if nums1_len > nums2_len:
            nums1, nums2, nums1_len, nums2_len = nums2, nums1, nums2_len, nums1_len

        min_, max_, half_len = 0, nums1_len, (nums1_len + nums2_len + 1) // 2

        while min_ <= max_:
            i = (min_ + max_) // 2
            j = half_len - i

            if i < nums1_len and nums2[j - 1] > nums1[i]:
                min_ = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                max_ = i - 1
            else:
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])

                if (nums1_len + nums2_len) % 2 == 1:
                    return max_left

                if i == nums1_len:
                    min_right = nums2[j]
                elif j == nums2_len:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])

                return (max_left + min_right) / 2.0

        return 0.0

