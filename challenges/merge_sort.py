# # Código de merge sort dado na aula 2.3 do dia
# # 31/05/23 pelo Professor Eli e adaptado para ser genérico


# def merge_sort(item):
#     if len(item) <= 1:
#         return item

#     mid = len(item) // 2
#     left, right = merge_sort(item[:mid]), merge_sort(item[mid:])

#     return merge(left, right)


# def merge(left, right):
#     merged = []
#     left_cursor, right_cursor = 0, 0

#     while left_cursor < len(left) and right_cursor < len(right):
#         if left[left_cursor] <= right[right_cursor]:
#             merged.append(left[left_cursor])
#             left_cursor += 1
#         else:
#             merged.append(right[right_cursor])
#             right_cursor += 1

#     merged.extend(left[left_cursor:])
#     merged.extend(right[right_cursor:])

#     return merged


# Código de merge sort dado na aula 2.3 do dia 31/05/23
# pelo Professor Eli e adaptado para string
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
