'''
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false


'''


# class Solution(object):
#     # 定义上下左右四个行走方向
#     directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
#         m = len(board)
#         if m == 0:
#             return False
#         n = len(board[0])
#         mark = [[0 for _ in range(n)] for _ in range(m)]
#
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] == word[0]:
#                     # 将该元素标记为已使用
#                     mark[i][j] = 1
#                     if self.backtrack(i, j, mark, board, word[1:]) == True:
#                         return True
#                     else:
#                         # 回溯
#                         mark[i][j] = 0
#         return False
#
#     def backtrack(self, i, j, mark, board, word):
#         if len(word) == 0:
#             return True
#
#         for direct in self.directs:
#             cur_i = i + direct[0]
#             cur_j = j + direct[1]
#
#             if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]) and board[cur_i][cur_j] == \
#                     word[0]:
#                 # 如果是已经使用过的元素，忽略
#                 if mark[cur_i][cur_j] == 1:
#                     continue
#                 # 将该元素标记为已使用
#                 mark[cur_i][cur_j] = 1
#                 if self.backtrack(cur_i, cur_j, mark, board, word[1:]) == True:
#                     return True
#                 else:
#                     # 回溯
#                     mark[cur_i][cur_j] = 0
#         return False

# class Solution:
#
#     def exist(self, board, word):
#         row, col = len(board), len(board[0])
#
#         def dfs(x, y, index):
#             if board[x][y] != word[index]:
#                 return False
#             if index == len(word) - 1:
#                 return True
#             board[x][y] = '#'
#             for choice in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
#                 nx, ny = x + choice[0], y + choice[1]
#                 if 0 <= nx < row and 0 <= ny < col and dfs(nx, ny, index + 1):
#                     return True
#             board[x][y] = word[index]
#
#         for i in range(row):
#             for j in range(col):
#                 if dfs(i, j, 0):
#                     return True
#         return False

# from typing import List
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#
#         def check(i: int, j: int, k: int) -> bool:
#             if board[i][j] != word[k]:
#                 return False
#             if k == len(word) - 1:
#                 return True
#
#             visited.add((i, j))
#             result = False
#             for di, dj in directions:
#                 newi, newj = i + di, j + dj
#                 if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
#                     if (newi, newj) not in visited:
#                         if check(newi, newj, k + 1):
#                             result = True
#                             break
#
#             visited.remove((i, j))
#             return result
#
#         h, w = len(board), len(board[0])
#         visited = set()
#         for i in range(h):
#             for j in range(w):
#                 if check(i, j, 0):
#                     return True
#         return False


class Solution:
    def exist(self, board, word):
        row, col = len(board), len(board[0])
        def dfs(x,y,index):
            if board[x][y] != word[index]:
                return False
            if index ==len(word)-1:
                return True
            board[x][y]='#'
            for choice in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx, ny = x + choice[0], y + choice[1]
                if 0<nx<row and 0<ny<col and dfs(nx,ny,index+1):
                    return True
            board[x][y]=word[index]

        for i in range(row):
            for j in range(col):
                if dfs(i,j,0)==True:
                    return True
        return False

