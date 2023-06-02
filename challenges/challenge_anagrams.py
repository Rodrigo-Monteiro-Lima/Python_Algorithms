def merge_sort_string(string: str) -> str:
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left, right = merge_sort_string(string[:mid]), merge_sort_string(
        string[mid:]
    )
    return merge_string(left, right)


def merge_string(left, right):
    merged = ""
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged += left[left_cursor]
            left_cursor += 1
        else:
            merged += right[right_cursor]
            right_cursor += 1

    for i in range(left_cursor, len(left)):
        merged += left[i]

    for i in range(right_cursor, len(right)):
        merged += right[i]

    return merged


def is_anagram(first_string, second_string):
    if (
        type(first_string) != str
        or type(second_string) != str
        or len(first_string) == 0
        and len(second_string) == 0
    ):
        return (first_string, second_string, False)

    first_string = merge_sort_string(first_string.lower())
    second_string = merge_sort_string(second_string.lower())

    if len(first_string) != len(second_string):
        return (first_string, second_string, False)

    for i in range(len(first_string)):
        if first_string[i] != second_string[i]:
            return (first_string, second_string, False)

    return (first_string, second_string, True)
