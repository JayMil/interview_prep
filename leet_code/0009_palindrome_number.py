
"""
9. Palindrome Number [Easy]

constraints
* 121 is a palindrome and 123 is not
* negative numbers are not palindromes
"""


class Solution:
    def isPalindrome(self, x: int):

        if x < 0:
            return False

        # return true for single digits
        if x / 10 < 1:
            return True

        if x % 10 == 0:
            return False

        y = 0
        while y < x:
            r = x % 10
            x = int(x/10)
            if x == y:
                return True
            y = (y * 10) + r

        return y == x


def assert_are_equal(actual, expected):
    assert actual == expected, f"Expected: '{expected}' but got '{actual}'"


def test_odd_palindrome():
    assert_are_equal(Solution().isPalindrome(10001), True)


def test_even_palindrome():
    assert_are_equal(Solution().isPalindrome(100001), True)


def test_two_digit_multiple_of_ten():
    assert_are_equal(Solution().isPalindrome(10), False)


def test_three_digit_multiple_of_ten():
    assert_are_equal(Solution().isPalindrome(100), False)


def test_negative():
    assert_are_equal(Solution().isPalindrome(-121), False)


def test_single_digit():
    assert_are_equal(Solution().isPalindrome(1), True)


def test_all_same_number():
    assert_are_equal(Solution().isPalindrome(1111), True)


if __name__ == '__main__':
    test_odd_palindrome()
    test_even_palindrome()
    test_two_digit_multiple_of_ten()
    test_three_digit_multiple_of_ten()
    test_negative()
    test_single_digit()
    test_all_same_number()


