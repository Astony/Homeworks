from typing import Generator, List, Tuple


class Board:
    """Class Board, that contains information about a tic tac toe board.

    :param board: The situation on tic tac board.
    :type board: List
    """

    @staticmethod
    def shape_board(board: List[List]) -> List[str]:
        """Special method for shaping 3D board to 1D board

        :param board: The situation on tic tac board.
        :type board: List[Lists]
        :return: 1D board
        :rtype: List[str]"""
        shaped_board = []
        for row in board:
            for element in row:
                shaped_board.append(element)
        return shaped_board

    def __init__(self, board: List[List]) -> None:
        self.board3D = board
        self.board1D = Board.shape_board(board)

    def rows(self) -> Generator[List, None, None]:
        """Generator of boards rows"""
        for row in self.board3D:
            yield row

    def columns(self) -> Generator[List, None, None]:
        """Generator of boards columns"""
        for index in range(2):
            yield self.board1D[index::3]

    def diagonals(self) -> Tuple:
        """Function return tuple with boards diagonals"""
        return self.board1D[::4], self.board1D[2:7:2]

    def enumerate_winning_position(self) -> Generator[List, None, None]:
        """Generator that yields rows and columns"""
        for position in self.rows():
            yield position
        for position in self.columns():
            yield position

    def check_board(self) -> str:
        """Function that analyze a situation on the tic tac toe

        :return: String that contains info about winner.
        :rtype: str"""
        for position in self.enumerate_winning_position():
            if len(set(position)) == 1 and position[0] != "-":
                return f"{position[0]} wins"
        for diagonal in self.diagonals():
            if len(set(diagonal)) == 1 and diagonal[0] != "-":
                return f"{diagonal[0]} wins"
        if "-" in self.board1D:
            return "unfinished"
        return "draw"
