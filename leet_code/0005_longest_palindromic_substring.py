"""
5. Longest Palindromic Substring

constraints
* no spaces
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        sLen = len(s)
        longestLen = 0
        longestWord = ""
        start = 0
        while start < sLen and longestLen < (((sLen-start+1)**2)+1):
            # odd
            l, r = start, start
            while l >= 0 and r < sLen and s[l] == s[r]:
                if r-l+1 > longestLen:
                    longestLen = r-l+1
                    longestWord = s[l:r+1]
                l -= 1
                r += 1

            # even
            l, r = start, start+1
            while l >= 0 and r < sLen and s[l] == s[r]:
                if r-l+1 > longestLen:
                    longestLen = r-l+1
                    longestWord = s[l:r+1]
                l -= 1
                r += 1

            start += 1

        return longestWord

    """
        This solution failed with Time Limit Exceeded.
        The time complexity of this solution is ~ o(n^3) as I will be looping over every combination
        of adjacent letters o(n^2) and then for each combination looping over half of those
        characters o(n/2) giving o(n/2) * o(n^2) which simplifies to around o(n^3)
        
        The above solution uses dynamic programming to iterate through each character determining if
        it is the center of a palindrome. It will loop through almost every charater o(n) and then for
        each character check if it is the center of a palindrome for both odd and even palindromes o(2n).
        This gives o(n) * o(2n) which simplifies to around o(n^2).
    """
    def longestPalindromeSlow(self, s: str) -> str:
        size = len(s)
        while size > 1:
            start = 0
            while (start + size - 1) < len(s):
                if self.isPalindrome(s[start:start+size]):
                    return s[start:start+size]
                start += 1
            size -= 1

        return s[0]

    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True


def assert_are_equal(actual, expected):
    assert actual == expected, f"Expected: '{expected}' but got '{actual}'"


def test_longest_in_first_characters():
    assert_are_equal(Solution().longestPalindrome("babad"), "bab")


def test_longest_in_last_characters():
    assert_are_equal(Solution().longestPalindrome("ribab"), "bab")


def test_longest_in_center_characters():
    assert_are_equal(Solution().longestPalindrome("rbabb"), "bab")


def test_whole_string_is_palindrome_even():
    assert_are_equal(Solution().longestPalindrome("abccba"), "abccba")


def test_whole_string_is_palindrome_odd():
    assert_are_equal(Solution().longestPalindrome("abcba"), "abcba")

def test_multiple_palindromes():
    assert_are_equal(Solution().longestPalindrome("ilibbabbllell"), "bbabb")


def test_no_palindromes():
    assert_are_equal(Solution().longestPalindrome("abcdefghijklmnopqrstuvwxyz1234567890"), "a")


def test_single_character():
    assert_are_equal(Solution().longestPalindrome("a"), "a")


if __name__ == '__main__':
    test_longest_in_first_characters()
    test_longest_in_last_characters()
    test_longest_in_center_characters()
    test_whole_string_is_palindrome_even()
    test_whole_string_is_palindrome_odd()
    test_multiple_palindromes()
    test_no_palindromes()
    test_single_character()
