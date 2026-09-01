nums1 =input("enter the nums 1-")
nums2 = input("enter  nums2- ")
count = ""
count1 = 0
for i in range(0,len(nums1)):
    if nums1[i] in nums2 and nums1[i] not in count:
       count += nums1[i]
       count1 += 1
       print(nums1[i])
for i in range(0,len(nums2)):
    if nums2[i] in nums1 and nums2[i] not in count:
       count += nums2[i]
       count1 += 1
       print(nums2[i])
print(f"there are {count1} common elements in two lists")
