def find_duplicate(nums=[]):
    try:
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1] and nums[i] >= 0:
                return nums[i]
        return False
    except TypeError:
        return False
