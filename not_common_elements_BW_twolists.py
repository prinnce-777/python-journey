nums1 =input("enter the nums 1-")
nums2 = input("enter  nums2- ")
count = ""
for i in range(0,len(nums1)):
    if nums1[i] not in nums2: #and nums1[i] not in count:
       count += nums1[i]
for j in range(0,len(nums2)):
    if nums2[j] not in nums1: #and nums1[i] not in count:
       count += nums2[j]
count = list(count)
print(count)
