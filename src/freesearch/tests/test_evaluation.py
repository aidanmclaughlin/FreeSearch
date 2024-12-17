"""
Tests for the evaluation module.
"""
import chess
from ..core.evaluation import evaluate_position, count_legal_moves

def test_evaluation_starting_position():
    """Test that the starting position evaluates to 0 (equal for both sides)."""
    board = chess.Board()
    assert evaluate_position(board) == 0

def test_count_legal_moves():
    """Test that legal move counting works correctly."""
    board = chess.Board()
    # Starting position should have 20 moves for white
    assert count_legal_moves(board) == 20

def test_evaluation_after_e4():
    """Test evaluation after 1.e4."""
    board = chess.Board()
    board.push_san("e4")
    # After e4, it's Black's turn and White has more moves
    # This is a negative score from Black's perspective
    assert evaluate_position(board) < 0
