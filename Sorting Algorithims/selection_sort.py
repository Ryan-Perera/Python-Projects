import get_list

nums = get_list.numbers()
# Traverse through all array elements
for i in range(len(nums)):

	min_index = i
	for j in range(i+1, len(nums)):
		if nums[min_index] > nums[j]:
			min_index = j
			
	nums[i], nums[min_index] = nums[min_index], nums[i]

print ("Sorted array")
print(nums)
