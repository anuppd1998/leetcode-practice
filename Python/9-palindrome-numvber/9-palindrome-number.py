# ONLY MATHEMATICS
def isPalindrome(x):

    if x < 0:
        return False
    
    original = x
    reversed_number = 0

    while x != 0:

        digit = x % 10
        reversed_number = reversed_number * 10 + digit
        x = x // 10

    return reversed_number == original

# PYTHONIC WAY
def isPalindrome(x):
    return str(x) == str(x)[::-1]