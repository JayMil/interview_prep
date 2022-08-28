
"""
3. Longest Substring Without Repeating Characters [Medium]
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        end = len(s)
        longestWord = ""
        word = ""
        letterSet = set()
        wordStartIndex = 0

        while (i + wordStartIndex) < end:
            letter = s[i + wordStartIndex]
            if letter not in letterSet:
                word += letter
                letterSet.add(letter)
                i += 1
                continue

            # letter is in word - reset
            if len(word) > len(longestWord):
                longestWord = word

            wordStartIndex = s.index(letter, wordStartIndex) + 1
            i = i - (word.index(letter) + 1) + 1
            word = s[wordStartIndex:(wordStartIndex+i)]
            letterSet = set(word)

        if len(word) > len(longestWord):
            longestWord = word


        return len(longestWord)


def test_longest_at_beginning():
    assert_are_equal(3, Solution().lengthOfLongestSubstring("abcabcbb"))


def test_longest_at_end():
    assert_are_equal(3, Solution().lengthOfLongestSubstring("aaaaabc"))


def test_all_same_characters():
    assert_are_equal(1, Solution().lengthOfLongestSubstring("bbbbb"))


def test_longest_in_middle_with_preceding_duplicate_character():
    assert_are_equal(3, Solution().lengthOfLongestSubstring("pwwkew"))


def test_longest_in_middle_with_preceding_duplicate_character_matching_middle_character():
    assert_are_equal(6, Solution().lengthOfLongestSubstring("bbtablud"))


def test_empty():
    assert_are_equal(0, Solution().lengthOfLongestSubstring(""))


def test_blank():
    assert_are_equal(1, Solution().lengthOfLongestSubstring(" "))


def assert_are_equal(actual, expected):
    assert actual == expected, f"Expected: '{expected}' but got '{actual}'"


if __name__ == '__main__':
    test_longest_at_beginning()
    test_longest_at_end()
    test_all_same_characters()
    test_longest_in_middle_with_preceding_duplicate_character()
    test_longest_in_middle_with_preceding_duplicate_character_matching_middle_character()
    test_empty()
    test_blank()
