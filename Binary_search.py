def search(self, nums, target):
    # Set the initial values for the low and high indices
    low = 0
    high = len(nums)-1
    
    # While the low index is less than or equal to the high index
    while low <= high:
        # Calculate the middle index
        mid = (high + low) // 2
        
        # If the middle element is the target, return its index
        if nums[mid] == target:
            return mid
        # If the middle element is greater than the target, search the left half
        elif nums[mid] > target:
            high = mid - 1
        # If the middle element is less than the target, search the right half
        else:
            low = mid + 1
    
    # If the target is not found, return -1
    return -1

