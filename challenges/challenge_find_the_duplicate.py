from challenges.merge_sort import merge_sort


def find_duplicate(nums=[]):
    if not isinstance(nums, list) or len(nums) == 0:
        return False

    for i in range(len(nums)):
        if not isinstance(nums[i], int) or nums[i] < 0:
            return False

    nums = merge_sort(nums)

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]

    return False
