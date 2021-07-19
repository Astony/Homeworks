import pytest

from homework7.task03.tic_tac_toe import tic_tac_toe_checker

x_wins = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]
o_wins = [["o", "-", "-"], ["o", "x", "-"], ["o", "x", "x"]]
x_diag_win = [["o", "-", "x"], ["o", "x", "-"], ["x", "-", "-"]]
unfinished_case = [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]
draw_case = [["o", "x", "o"], ["x", "x", "o"], ["x", "o", "x"]]


@pytest.mark.parametrize(
    "board, result",
    [
        (x_wins, "x wins"),
        (o_wins, "o wins"),
        (x_diag_win, "x wins"),
        (unfinished_case, "unfinished"),
        (draw_case, "draw"),
    ],
)
def test_positive_cases(board, result):
    assert tic_tac_toe_checker(board) == result
