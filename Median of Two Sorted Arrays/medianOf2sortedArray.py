import sys

class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1, nums2):

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        start = 0
        end = min(len(nums1), len(nums2)) - 1

        def obtain_partition(median):
            LH1 = median

            LH2 = int(len(nums1 + nums2) * 0.5) - LH1 - 1

            if len(nums1 + nums2) % 2 == 0:
                LH2 -= 1
            RH1 = LH1 + 1
            RH2 = LH2 + 1
            return LH1, LH2, RH1, RH2

        mid = start - int((start - end) * 0.5)
        LH1, LH2, RH1, RH2 = obtain_partition(mid)

        while LH1 >= 0 and RH1 <= len(nums1) - 1:
            if (nums1[LH1] <= nums2[RH2]) & (nums2[LH2] <= nums1[RH1]):
                if len(nums1 + nums2) % 2 != 0:
                    return max(nums1[LH1], nums2[LH2])
                else:
                    return (max(nums1[LH1], nums2[LH2]) + min(nums1[RH1], nums2[RH2])) * 0.5
                break
            elif nums1[LH1] >= nums2[RH2]:
                end = mid - 1
            else:
                start = mid + 1
            mid = (start + end) // 2
            LH1, LH2, RH1, RH2 = obtain_partition(mid)

        if len(nums1) <= 1:
            median_index = (len(nums2) - 1) // 2
            median_ = (nums2[median_index] + nums2[median_index + 1]) * 0.5 if len(nums2) % 2 == 0 else nums2[
                median_index]
            x = 0 if len(nums1) == 0 else nums1[0]
            if len(nums2) == 1 and len(nums1) == 1:
                return (nums2[0] + nums1[0]) * 0.5
            if x == median_ or len(nums1) == 0:
                return median_
            elif x <= median_:
                if len(nums2) % 2 == 0:
                    nums2[median_index - 1] = nums2[median_index]
                return (max(nums2[median_index - 1], nums1[0]) + nums2[median_index]) * 0.5
            else:
                if len(nums2) % 2 == 0:
                    nums2[median_index] = nums2[median_index + 1]
                return (nums2[median_index] + min(nums2[median_index + 1], nums1[0])) * 0.5

        elif len(nums1 + nums2) % 2 == 0:
            x1 = sys.maxsize * -1 if LH1 == -1 else nums1[LH1]
            x2 = sys.maxsize * -1 if LH2 == -1 else nums2[LH2]
            y1 = sys.maxsize if RH1 == len(nums1) else nums1[RH1]
            y2 = sys.maxsize if RH2 == len(nums2) else nums2[RH2]
            return (max(x1, x2) + min(y1, y2)) * 0.5
        else:
            if len(nums1) == RH1:
                return max(nums2[LH2], nums1[LH1])
            else:
                return nums2[LH2]


calling_class = Solution()
result = calling_class.findMedianSortedArrays([4, 3, 3, 7], [1,2,3])
print(result)