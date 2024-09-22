import tkinter as tk
from tkinter import messagebox

def minimax(board, depth, is_maximizing, player, opponent):
    score = evaluate_board(board, player, opponent)
    if score != 0:
        return score
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = player
                    score = minimax(board, depth + 1, False, player, opponent)
                    board[i][j] = ''
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = opponent
                    score = minimax(board, depth + 1, True, player, opponent)
                    board[i][j] = ''
                    best_score = min(score, best_score)
        return best_score

def evaluate_board(board, player, opponent):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return 1 if board[i][0] == player else -1
        if board[0][i] == board[1][i] == board[2][i] != '':
            return 1 if board[0][i] == player else -1
    if board[0][0] == board[1][1] == board[2][2] != '':
        return 1 if board[0][0] == player else -1
    if board[0][2] == board[1][1] == board[2][0] != '':
        return 1 if board[0][2] == player else -1
    return 0

def is_draw(board):
    return all(cell != '' for row in board for cell in row)

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Крестики - нолики')
        self.game = TicTacToeGame()

        window_width = 380
        window_height = 430
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        self.board_frame = tk.Frame(self.root, borderwidth=1, relief="solid")
        self.board_frame.pack(padx=10, pady=(10, 0))

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.board_frame, text='', width=5, height=2, bg="thistle", font = ("Arial", 20, "bold"),
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

        self.selection_frame = tk.Frame(self.root)
        self.selection_frame.pack(pady=10)

        self.opponent_button = tk.Button(self.selection_frame, text='Выбор противника', width = 24, height = 2, font = ("Consolas", 12), command=self.select_opponent)
        self.opponent_button.pack()

        self.opponent_label = tk.Label(self.selection_frame, text='', width = 24, height = 2, font = ("Consolas", 12))
        self.opponent_label.pack()

    def on_button_click(self, row, col):
        if self.game.make_move(row, col, self.game.current_player):
            button = self.buttons[row][col]
            button.config(text=self.game.current_player,
                          bg="pink" if self.game.current_player == 'X' else "moccasin",
                          state="disabled")
            if self.game.check_winner(self.game.current_player):
                messagebox.showinfo("Победа",
                                    f"Победили {'крестики' if self.game.current_player == 'X' else 'нолики'}!")
                self.reset_game()
            elif self.game.is_draw():
                messagebox.showinfo("Ничья", "Ничья!")
                self.reset_game()
            else:
                if self.game.opponent == 'human':
                    self.game.switch_player()
                else:
                    self.play_computer_move()

    def play_computer_move(self):
        row, col = self.game.computer_move()
        self.game.make_move(row, col, 'O')
        button = self.buttons[row][col]
        button.config(text='O', bg="moccasin", state="disabled")
        if self.game.check_winner('O'):
            messagebox.showinfo("Победа", "Победил компьютер!")
            self.reset_game()
        elif self.game.is_draw():
            messagebox.showinfo("Ничья", "Ничья!")
            self.reset_game()

    def select_opponent(self):
        self.opponent_button.config(state="disabled")

        response = messagebox.askquestion("Выбор противника", "Играть с компьютером?")
        self.opponent_button.pack(padx=10, pady=10)
        if response == 'yes':
            self.game.opponent = 'computer'
            self.opponent_label.config(text="Игра против компьютера", bg="palegreen3")
        else:
            self.game.opponent = 'human'
            self.opponent_label.config(text="Игра против человека", bg="palegreen3")

    def reset_game(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text='', bg="thistle", state="normal")
        self.game.reset_board()
        self.opponent_button.config(state="normal", bg="SystemButtonFace")
        self.opponent_label.config(text='')

class TicTacToeGame:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.opponent = None

    def make_move(self, row, col, player):
        if self.board[row][col] == '':
            self.board[row][col] = player
            return True
        return False

    def switch_player(self):
        if self.opponent == 'human':
            if self.current_player == 'X':
                self.current_player = '0'
            else:
                self.current_player = 'X'

    def check_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) \
               or all(self.board[j][i] == player for j in range(3)):
                return True
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == player) \
           or (self.board[0][2] == self.board[1][1] == self.board[2][0] == player):
            return True
        return False

    def is_draw(self):
        return all(self.board[row][col] != '' for row in range(3) for col in range(3))

    def computer_move(self):
        best_score = -float('inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    self.board[i][j] = 'O'
                    score = minimax(self.board, 0, False, 'O', 'X')
                    self.board[i][j] = ''
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move

    def reset_board(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
