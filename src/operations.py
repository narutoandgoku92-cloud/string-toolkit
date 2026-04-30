def reverse_text(text):
    return text[::-1]

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def replace_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join('#' if char in vowels else char for char in text)

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]