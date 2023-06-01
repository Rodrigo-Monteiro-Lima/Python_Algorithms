def is_palindrome_iterative(word=""):
    if word == "" or len(word) == 0 or type(word) != str:
        return False

    reversed_word = word[::-1]

    if word.lower() == reversed_word.lower():
        return True

    return False
