"""
Evaluation module for the chess engine.
Implements position evaluation based on the difference in legal moves between players.
"""
from typing import List
import chess

def count_legal_moves(board: chess.Board) -> int:
    """Count the number of legal moves in the current position."""
    return len(list(board.legal_moves))

def evaluate_position(board: chess.Board) -> float:
    """
    Evaluate the position based on the difference in legal moves between players.
    Returns evaluation from the perspective of the side to move.

    Args:
        board: Current chess position

    Returns:
        float: Positive score if side to move has more moves, negative if opponent has more
    """
    # Make a copy to avoid modifying the original board
    temp_board = board.copy()

    # Count moves for the side to move
    side_to_move_moves = count_legal_moves(temp_board)

    # Switch sides and count opponent moves
    temp_board.turn = not temp_board.turn
    opponent_moves = count_legal_moves(temp_board)

    # Return difference from side to move's perspective
    return float(side_to_move_moves - opponent_moves)
