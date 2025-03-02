class Solution:

    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]])-> List[List[int]]:

        result = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:
                result.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                result.append(nums1[i])
                i += 1

            else:
                result.append(nums2[j])
                j += 1
        

        while i < len(nums1):
            result.append(nums1[i])
            i += 1
        
        while j < len(nums2):
            result.append(nums2[j])
            j += 1

        print(result)


        return result
    
    def mergeArrays1(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        hashMap = set()

        n = max(len(nums1), len(nums2))
        print(n)
        for i in range(n):
            if i <= len(nums1) - 1:
                if nums1[i][0] not in hashMap:
                    hashMap.add(nums1[i][0])

            if i <= len(nums2) - 1:
                if nums2[i][0] not in hashMap:
                    hashMap.add(nums2[i][0])

        result = []

        x = 0
        y = 0
        for ind, idx in enumerate(hashMap):
            val = 0
            if x <= len(nums1) - 1:
                if idx == nums1[x][0]:
                    val += nums1[x][1]
                    x += 1

            if y <= len(nums2) - 1:
                print("y:", y)
                if idx == nums2[y][0]:
                    val += nums2[y][1]
                    y += 1

            result.append([idx, val])

        return result
