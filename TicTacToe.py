class TicTacToe:
    @staticmethod
    def creating_board():
        """Creates an empty Tic-Tac-Toe board."""
        return ['.'] * 9

    @staticmethod
    def print_board(board):
        """Prints the board in a 3x3 format."""
        for i in range(3):
            print(" ".join(board[i * 3:(i + 1) * 3]))
        print()

    @staticmethod
    def evaluate(board):
        """Evaluates the board and returns:
        1 if 'X' (AI) wins, -1 if 'O' (Player) wins, 0 otherwise."""
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] == 'X':
                return 1  # AI wins
            elif board[combo[0]] == board[combo[1]] == board[combo[2]] == 'O':
                return -1  # Player wins
        return 0  # Draw

    @staticmethod
    def is_draw(board):
        """Returns True if the board is full and there is no winner."""
        return '.' not in board and TicTacToe.evaluate(board) == 0

    @staticmethod
    def alpha_beta_pruning(board, depth, alpha, beta, maximizing):
        """
        Implements the Minimax algorithm with Alpha-Beta Pruning.
        Returns the best score and the best move.
        """
        score = TicTacToe.evaluate(board)
        
        # Base cases: AI wins, Player wins, Draw or depth limit reached
        if score == 1 or score == -1 or TicTacToe.is_draw(board) or depth == 0:
            return score, None
        
        if maximizing:  # AI's turn (Maximizing)
            best_score = float('-inf')
            best_move = None
            for i in range(9):
                if board[i] == '.':
                    new_board = board[:]
                    new_board[i] = 'X'
                    eval_score, _ = TicTacToe.alpha_beta_pruning(
                        new_board, depth - 1, alpha, beta, False
                    )
                    if eval_score > best_score:
                        best_score = eval_score
                        best_move = i
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
            return best_score, best_move
        else:  # Human's turn (Minimizing)
            best_score = float('inf')
            best_move = None
            for i in range(9):
                if board[i] == '.':
                    new_board = board[:]
                    new_board[i] = 'O'
                    eval_score, _ = TicTacToe.alpha_beta_pruning(
                        new_board, depth - 1, alpha, beta, True
                    )
                    if eval_score < best_score:
                        best_score = eval_score
                        best_move = i
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break  # cut-off
            return best_score, best_move

    @staticmethod
    def game():
        """Runs the Tic-Tac-Toe game loop."""
        board = TicTacToe.creating_board()
        turn = True
        
        while True:
            TicTacToe.print_board(board)
            
            if TicTacToe.evaluate(board) == 1:
                print("AI wins!")
                break
            elif TicTacToe.evaluate(board) == -1:
                print("Player wins!")
                break
            elif TicTacToe.is_draw(board):
                print("It's a draw!")
                break
                
            if turn:
                while True:
                    move = input("Enter your move (1-9): ")
                    if move.isdigit():
                        move = int(move)
                        if 1 <= move <= 9 and board[move - 1] == '.':
                            board[move - 1] = 'O'
                            turn = False
                            break
                    print("Invalid move. Try again.")
            else:
                # AI's move
                _, move = TicTacToe.alpha_beta_pruning(board, 9, float('-inf'), float('inf'), True)
                if move is not None:
                    board[move] = 'X'
                    turn = True