import tkinter as tk
import math

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.buttons = []

        self.create_ui()

    def create_ui(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text=" ", font=("Arial", 24), height=2, width=5,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def on_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == " " and self.current_player == "X":
            self.board[index] = "X"
            self.buttons[row][col].config(text="X")
            if self.check_winner("X"):
                self.show_winner("Você venceu!")
                return
            elif " " not in self.board:
                self.show_winner("Empate!")
                return
            self.current_player = "O"
            self.ai_move()

    def ai_move(self):
        best_score = -math.inf
        best_move = None
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                score = self.minimax(self.board, 0, False)
                self.board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i

        if best_move is not None:
            self.board[best_move] = "O"
            row, col = divmod(best_move, 3)
            self.buttons[row][col].config(text="O")
            if self.check_winner("O"):
                self.show_winner("A IA venceu!")
                return
            elif " " not in self.board:
                self.show_winner("Empate!")
                return
            self.current_player = "X"

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner("O"):
            return 1
        if self.check_winner("X"):
            return -1
        if " " not in board:
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if board[i] == " ":
                    board[i] = "O"
                    score = self.minimax(board, depth + 1, False)
                    board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if board[i] == " ":
                    board[i] = "X"
                    score = self.minimax(board, depth + 1, True)
                    board[i] = " "
                    best_score = min(score, best_score)
            return best_score

    def check_winner(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
            [0, 4, 8], [2, 4, 6]             # Diagonais
        ]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

    def show_winner(self, message):
        winner_label = tk.Label(self.window, text=message, font=("Arial", 18))
        winner_label.grid(row=3, column=0, columnspan=3)
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()