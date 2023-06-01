from challenges.merge_sort import merge_sort


def find_duplicate(nums=[]):
    if type(nums) != list or len(nums) == 0:
        return False

    nums = merge_sort(nums)

    # for i in range(len(nums)):
    #      if type(num) != int or num < 0 or i == len(nums) - 1:
    #         return False
    #     if nums[i] in nums[i + 1 :]:
    #         return nums[i]
    # return False
    for i, num in enumerate(nums):
        if type(num) != int or num < 0 or i == len(nums) - 1:
            return False
        if nums[i] == nums[i + 1]:
            return num

    return False
