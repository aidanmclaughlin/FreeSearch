"""
Main entry point for the FreeSearch chess engine.
Implements UCI protocol interface and command handling loop.
"""
from .uci.protocol import UCIEngine

def main():
    """
    Main entry point for the chess engine.
    Implements UCI protocol command loop.
    """
    engine = UCIEngine()
    while True:
        try:
            command = input()
            response = engine.handle_command(command.strip())
            if response:
                print(response, flush=True)
            if response == "quit":
                break
        except EOFError:
            break
        except Exception as e:
            # Log any unexpected errors but don't crash
            print(f"info string Error: {str(e)}", flush=True)

if __name__ == "__main__":
    main()
