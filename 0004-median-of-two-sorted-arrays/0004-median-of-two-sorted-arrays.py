class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        l = m+n
        if l==0:
            return 0
        elif l%2==0:
            n1 = l/2
            n2 = l/2+1
        else:
            n1 = (l+1)/2
            n2 = -1
        
        count=0
        i1 = 0
        i2 = 0
        num1 = num2 = None
        x = 0
        limit = max(n1, n2)

        while count < limit:
            if i1 == m:
                a = float(inf)
            else:
                a = nums1[i1]
            if i2 == n:
                b = float(inf)
            else:
                b = nums2[i2]

            if a <= b:
                i1+=1
                x = nums1[i1-1]
            else:
                i2+=1
                x = nums2[i2-1]
            count+=1 
            if count == n1:
                num1 = x
                if n2 == -1:
                    return num1
            elif count == n2:
                num2 = x
                return (num1 + num2)/2
        
        return 0