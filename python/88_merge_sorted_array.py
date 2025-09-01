from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        i = m-1
        j = n-1
        index = m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[index] = nums1[i]
                i -= 1
            else:
                nums1[index] = nums2[j]
                j -= 1
            index -= 1
        while i >= 0:
            nums1[index] = nums1[i]
            index -= 1
            i -= 1
        while j >= 0:
            nums1[index] = nums2[j]
            j -= 1
            index -= 1




if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    solution.merge(nums1, 3, nums2, 3)
    print(nums1)

    nums1 = [1]
    nums2 = []
    solution.merge(nums1, 1, nums2, 0)
    print(nums1)

    nums1 = [0]
    nums2 = [1]
    solution.merge(nums1, 0, nums2, 1)
    print(nums1)

