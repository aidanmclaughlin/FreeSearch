"""
UCI protocol implementation for the chess engine.
Handles standard UCI commands and interfaces with the search algorithm.
"""
from typing import Optional, List
import chess
from ..core.search import alpha_beta_search, find_best_move

class UCIEngine:
    """UCI chess engine implementation."""

    def __init__(self):
        """Initialize the UCI engine with a new board."""
        self.board = chess.Board()
        self.searching = False
        self.name = "FreeSearch"
        self.author = "Devin"

    def handle_command(self, command: str) -> str:
        """
        Handle UCI protocol commands.

        Args:
            command: UCI command string

        Returns:
            Response string for the UCI interface
        """
        if command == "uci":
            return self._handle_uci()
        elif command == "isready":
            return "readyok"
        elif command.startswith("position"):
            self._handle_position(command)
            return ""
        elif command.startswith("go"):
            return self._handle_go(command)
        elif command == "quit":
            return "quit"
        return ""

    def _handle_uci(self) -> str:
        """Handle the UCI identification command."""
        return f"id name {self.name}\nid author {self.author}\nuciok"

    def _handle_position(self, command: str) -> None:
        """
        Handle the position command.

        Supports both 'startpos' and FEN notation with optional moves.
        """
        parts = command.split()
        if "startpos" in command:
            self.board = chess.Board()
            move_index = command.find("moves")
            if move_index >= 0:
                moves = command[move_index:].split()[1:]
                for move in moves:
                    self.board.push_uci(move)
        elif "fen" in command:
            fen_parts = []
            i = parts.index("fen") + 1
            while i < len(parts) and parts[i] != "moves":
                fen_parts.append(parts[i])
                i += 1
            self.board = chess.Board(" ".join(fen_parts))
            if "moves" in parts:
                moves = parts[parts.index("moves")+1:]
                for move in moves:
                    self.board.push_uci(move)

    def _handle_go(self, command: str) -> str:
        """
        Handle the go command.

        Currently uses a fixed depth of 4 for all searches.
        Returns the best move in UCI format.
        """
        # Simple implementation with fixed depth
        best_move = find_best_move(self.board, depth=4)
        return f"bestmove {best_move.uci()}"

    def _parse_time_control(self, command: str) -> dict:
        """
        Parse time control parameters from go command.

        Currently unused as we use fixed depth, but included for future extensions.
        """
        params = command.split()
        time_params = {}
        for param, value in zip(params, params[1:]):
            if param in ["wtime", "btime", "winc", "binc", "movestogo"]:
                time_params[param] = int(value)
        return time_params
