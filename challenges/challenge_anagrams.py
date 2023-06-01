from challenges.merge_sort import merge_sort


def is_anagram(first_string, second_string):
    if (
        type(first_string) != str
        or type(second_string) != str
        or len(first_string) == 0
        and len(second_string) == 0
    ):
        return (first_string, second_string, False)

    first_string = "".join(merge_sort(first_string.lower()))
    second_string = "".join(merge_sort(second_string.lower()))

    if len(first_string) != len(second_string):
        return (first_string, second_string, False)

    for i in range(len(first_string)):
        if first_string[i] != second_string[i]:
            return (first_string, second_string, False)

    return (first_string, second_string, True)
