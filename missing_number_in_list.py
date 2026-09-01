nums = [1,2,3,4,6]
n = int(nums[len(nums) - 1])
sum = n * (n + 1) // 2
sum1 = 0
for i in range(0,len(nums)):
    sum1 += int(nums[i])
sum2 = sum - sum1
print("The missing number is", sum2)