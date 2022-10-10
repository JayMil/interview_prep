from typing import *

"""
36. Valid Sudoku

constraints
* board.length == 9
* board[i].length == 9
* board[i][j] is a digit 1-9 or "."

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rs = row set, cs = column set, bs = box set
        dictSets = dict()

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                current_row_set, current_column_set, current_box_set = self.get_sets(i, j, dictSets)

                if not self.add_to_set(board[i][j], current_row_set):
                    return False

                if not self.add_to_set(board[i][j], current_column_set):
                    return False

                if not self.add_to_set(board[i][j], current_box_set):
                    return False

        return True

    def get_sets(self, i: int, j: int, dictSets: dict[str, set]):
        # rs = row set, cs = column set, bs = box set
        # there are 9 of each type of set to validate
        current_row_set = None
        current_column_set = None
        current_box_set = None
        if i == 0:
            current_row_set = self.get_set("r1", dictSets)
        elif i == 1:
            current_row_set = self.get_set("r2", dictSets)
        elif i == 2:
            current_row_set = self.get_set("r3", dictSets)
        elif i == 3:
            current_row_set = self.get_set("r4", dictSets)
        elif i == 4:
            current_row_set = self.get_set("r5", dictSets)
        elif i == 5:
            current_row_set = self.get_set("r6", dictSets)
        elif i == 6:
            current_row_set = self.get_set("r7", dictSets)
        elif i == 7:
            current_row_set = self.get_set("r8", dictSets)
        elif i == 8:
            current_row_set = self.get_set("r9", dictSets)

        if j == 0:
            current_column_set = self.get_set("c1", dictSets)
        elif j == 1:
            current_column_set = self.get_set("c2", dictSets)
        elif j == 2:
            current_column_set = self.get_set("c3", dictSets)
        elif j == 3:
            current_column_set = self.get_set("c4", dictSets)
        elif j == 4:
            current_column_set = self.get_set("c5", dictSets)
        elif j == 5:
            current_column_set = self.get_set("c6", dictSets)
        elif j == 6:
            current_column_set = self.get_set("c7", dictSets)
        elif j == 7:
            current_column_set = self.get_set("c8", dictSets)
        elif j == 8:
            current_column_set = self.get_set("c9", dictSets)

        if i // 3 == 0:
            if j // 3 == 0:
                current_box_set = self.get_set("b1", dictSets)
            elif j // 3 == 1:
                current_box_set = self.get_set("b2", dictSets)
            else:
                current_box_set = self.get_set("b3", dictSets)
        elif i // 3 == 1:
            if j // 3 == 0:
                current_box_set = self.get_set("b4", dictSets)
            elif j // 3 == 1:
                current_box_set = self.get_set("b5", dictSets)
            else:
                current_box_set = self.get_set("b6", dictSets)
        else:
            if j // 3 == 0:
                current_box_set = self.get_set("b7", dictSets)
            elif j // 3 == 1:
                current_box_set = self.get_set("b8", dictSets)
            else:
                current_box_set = self.get_set("b9", dictSets)

        return current_row_set, current_column_set, current_box_set

    def get_set(self, key: str, dictSets: dict[str, set]):
        # get the set from the dictionary if it exists,
        # otherwise create the set, add it to the dictionary, and return it
        if key not in dictSets:
            dictSets[key] = set()

        return dictSets[key]


    def add_to_set(self, value: str, sett: Set) -> bool:
        if value in sett:
            return False
        else:
            sett.add(value)
            return True


def assert_are_equal(actual, expected):
    assert actual == expected, f"Expected: '{expected}' but got '{actual}'"


def test_base_case():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert_are_equal(Solution().isValidSudoku(board), True)

def test_invalid_b1():
    board =  [["9", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert_are_equal(Solution().isValidSudoku(board), False)

def test_invalid_b2():
    board =  [["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", "7", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert_are_equal(Solution().isValidSudoku(board), False)


def test_invalid_b3():
    board =  [["5", "3", ".", ".", "7", ".", "6", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert_are_equal(Solution().isValidSudoku(board), False)


def test_invalid_b4():
    board =  [["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", "7", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert_are_equal(Solution().isValidSudoku(board), False)


def test_invalid_b5():
    board =  [["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", "2", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert_are_equal(Solution().isValidSudoku(board), False)


def test_invalid_b6():
    board =  [["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", "1", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert_are_equal(Solution().isValidSudoku(board), False)


if __name__ == '__main__':
    test_base_case()
    test_invalid_b1()
    test_invalid_b2()
    test_invalid_b3()
    test_invalid_b4()
    test_invalid_b5()
    test_invalid_b6()
