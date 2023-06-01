def is_palindrome_recursive(word=None, low_index=None, high_index=None):
    if word is None or word == "" or low_index is None or high_index is None:
        return False

    if low_index > high_index:
        return True

    if word[low_index].lower() != word[high_index].lower():
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
