from challenges.merge_sort import merge_sort


def find_duplicate(nums=[]):
    try:
        nums = merge_sort(nums)

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1] and nums[i] >= 0:
                return nums[i]

        return False
    except TypeError:
        return False


print(find_duplicate([1]))
