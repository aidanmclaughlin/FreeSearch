"""
Search module for the chess engine.
Implements alpha-beta pruning search algorithm with a fixed depth.
"""
from typing import Tuple, Optional
import chess
from .evaluation import evaluate_position

def alpha_beta_search(board: chess.Board, depth: int, alpha: float = float('-inf'),
                     beta: float = float('inf'), maximizing: bool = True) -> Tuple[float, Optional[chess.Move]]:
    """
    Alpha-beta pruning search implementation.

    Args:
        board: Current chess position
        depth: Remaining depth to search
        alpha: Alpha value for pruning
        beta: Beta value for pruning
        maximizing: True if maximizing player, False if minimizing

    Returns:
        Tuple of (evaluation score, best move found)
    """
    if depth == 0 or board.is_game_over():
        return evaluate_position(board), None

    best_move = None
    if maximizing:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = alpha_beta_search(board, depth - 1, alpha, beta, False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = alpha_beta_search(board, depth - 1, alpha, beta, True)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def find_best_move(board: chess.Board, depth: int = 4) -> chess.Move:
    """
    Find the best move in the current position.

    Args:
        board: Current chess position
        depth: Search depth (default: 4)

    Returns:
        Best move found
    """
    _, best_move = alpha_beta_search(board, depth)
    if best_move is None:
        # If no best move found (shouldn't happen in normal play),
        # return first legal move
        return next(board.legal_moves)
    return best_move
