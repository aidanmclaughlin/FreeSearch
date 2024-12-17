"""
Tests for the search module.
"""
import chess
from ..core.search import alpha_beta_search, find_best_move

def test_find_best_move():
    """Test that find_best_move returns a valid move."""
    board = chess.Board()
    move = find_best_move(board)
    assert isinstance(move, chess.Move)
    assert move in board.legal_moves

def test_alpha_beta_search():
    """Test that alpha-beta search returns both evaluation and move."""
    board = chess.Board()
    score, move = alpha_beta_search(board, depth=2)
    assert isinstance(score, float)
    assert isinstance(move, chess.Move)
    assert move in board.legal_moves
