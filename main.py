# Tic-Tac-Toe using Alpha-Beta Pruning
# Player is 'O' and AI is 'X'

import tkinter as tk
from tkinter import messagebox
from TicTacToe import TicTacToe

def reset_board(buttons):
    board = TicTacToe.creating_board()
    for button in buttons:
        button.config(text='', state=tk.NORMAL)
    return board

def check_game_status(board,buttons):
    result = TicTacToe.evaluate(board)
    if result == 1:
        messagebox.showinfo("Game Over", "AI wins!")
        board = reset_board(buttons)
        return True
    elif result == -1:
        messagebox.showinfo("Game Over", "You win!")
        board = reset_board(buttons)
        return True
    elif TicTacToe.is_draw(board):
        messagebox.showinfo("Game Over", "It's a draw!")
        board = reset_board(buttons)
        return True
    return False


def on_click(index, board, buttons):
    if board[index] == '.' and TicTacToe.evaluate(board) == 0:
        board[index] = 'O'
        buttons[index].config(text='O', state=tk.DISABLED, disabledforeground='green')
        if check_game_status(board,buttons):
            return
            
        _, ai_move = TicTacToe.alpha_beta_pruning(board, 9, float('-inf'), float('inf'), True)
        if ai_move is not None:
            board[ai_move] = 'X'
            buttons[ai_move].config(text='X', state=tk.DISABLED, disabledforeground='red')
            check_game_status(board,buttons)

def run_tic_tac_toe_gui():
    board = TicTacToe.creating_board()
    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    buttons = []
    for i in range(9):
        btn = tk.Button(root, text='', font=('Arial', 24), width=5, height=2,
                         command=lambda i=i: on_click(i, board, buttons))
        btn.grid(row=i//3, column=i%3)
        buttons.append(btn)
    
    root.mainloop()


if __name__ == "__main__":
    run_tic_tac_toe_gui()