from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    diag1 = ""
    diag2 = ""
    for i in range(3):
        diag1 += board[i][i]
        diag2 += board[i][2 - i]
        if board[i][0] == board[i][1] == board[i][2]:
            return f"{board[i][0]} wins"
        elif board[0][i] == board[1][i] == board[2][i]:
            return f"{board[0][i]} wins"
    for diag in diag1, diag2:
        if diag == diag[0] * 3:
            return f"{diag[0]} wins"
    for element in board:
        if "-" in element:
            return "unfinished"
    return "draw"
