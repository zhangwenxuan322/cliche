# 289. Game of Life
import copy
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        new_board = []
        for i in range(len(board)):
            tmp = []
            for j in range(len(board[0])):
                cur = board[i][j]
                live_count = 0
                for x in range(-1, 2):
                    tmp_x = i + x
                    for y in range(-1, 2):
                        tmp_y = j + y
                        if tmp_x < 0 or tmp_y < 0 or tmp_x == len(board) or tmp_y == len(board[0]) \
                                or (tmp_x == i and tmp_y == j):
                            continue
                        if board[tmp_x][tmp_y] == 1:
                            live_count += 1
                if cur == 1 and live_count < 2:
                    tmp.append(0)
                elif cur == 1 and live_count in (2, 3):
                    tmp.append(1)
                elif cur == 1 and live_count > 3:
                    tmp.append(0)
                elif cur == 0 and live_count == 3:
                    tmp.append(1)
                else:
                    tmp.append(0)
            new_board.append(tmp)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = new_board[i][j]

    def test(self):
        board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        self.gameOfLife(board)
        assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
        board = [[1, 1], [1, 0]]
        self.gameOfLife(board)
        assert board == [[1, 1], [1, 1]]
        print("all tests passed!")


Solution().test()
