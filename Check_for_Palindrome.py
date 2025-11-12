def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    reversed_str = cleaned[::-1]
    print("Original:", s)
    print("Cleaned:", cleaned)
    print("Reversed:", reversed_str)
    return cleaned == reversed_str

print(is_palindrome("hello"))

print(is_palindrome("A man a plan a canal Panama"))