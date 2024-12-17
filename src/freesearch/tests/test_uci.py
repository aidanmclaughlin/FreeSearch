"""
Tests for the UCI protocol implementation.
"""
import chess
from ..uci.protocol import UCIEngine

def test_uci_identification():
    """Test UCI identification command."""
    engine = UCIEngine()
    response = engine.handle_command("uci")
    assert response.startswith("id name")
    assert "FreeSearch" in response
    assert "uciok" in response

def test_isready():
    """Test isready command."""
    engine = UCIEngine()
    assert engine.handle_command("isready") == "readyok"

def test_position_startpos():
    """Test position command with startpos."""
    engine = UCIEngine()
    engine.handle_command("position startpos")
    assert engine.board == chess.Board()

def test_position_with_moves():
    """Test position command with moves."""
    engine = UCIEngine()
    engine.handle_command("position startpos moves e2e4")
    expected_board = chess.Board()
    expected_board.push_uci("e2e4")
    assert engine.board == expected_board

def test_go_command():
    """Test go command returns a valid move."""
    engine = UCIEngine()
    engine.handle_command("position startpos")
    response = engine.handle_command("go")
    assert response.startswith("bestmove")
    # Verify the move is in UCI format (e.g., "e2e4")
    assert len(response.split()[1]) == 4
