class Solution:

    # time: O(m + n)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1


   

    # BRute
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        merged = [0] * (m + n)
        left = 0
        right = 0
        index = 0

        """ Insert elements from nums1 and nums2 into
        merged array using left and right pointers """
        while left < m and right < n:
            if nums1[left] <= nums2[right]:
                merged[index] = nums1[left]
                left += 1
            else:
                merged[index] = nums2[right]
                right += 1
            index += 1

        # If right pointer reaches the end of nums2:
        while left < m:
            merged[index] = nums1[left]
            left += 1
            index += 1

        # If left pointer reaches the end of nums1:
        while right < n:
            merged[index] = nums2[right]
            right += 1
            index += 1

        """ Copy elements from merged array
        array back to nums1 """
        for i in range(m + n):
            nums1[i] = merged[i]