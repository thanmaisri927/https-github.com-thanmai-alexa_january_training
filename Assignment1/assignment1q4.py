def remove_even(nums):
    return [num for num in nums if num % 2 != 0]

# Test call
nums = [1,2,3,4,5,6,7,8,9,10]
print(remove_even(nums))  # Output: [1, 3, 5, 7, 9]
