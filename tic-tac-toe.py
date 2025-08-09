import tkinter as tk
from tkinter import messagebox
from tkinter import font

class TicTacToe:
    def __init__(self, root):
        root.title("Крестики-нолики")
        self.current_player = "X"
        self.board = [" " for _ in range(9)]

        # Настройка шрифта
        self.custom_font = font.Font(family="Times New Roman", size=25, weight="bold")

        # Цвета для игроков
        self.player_colors = {"X": "red", "O": "blue"}

        # Создаем кнопки для игрового поля
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    root,
                    text=" ",
                    font=self.custom_font,
                    width=5,
                    height=2,
                    fg="black",
                    command=lambda row=i, col=j: self.on_click(row, col)
                )
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def on_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(
                text=self.current_player,
                fg=self.player_colors[self.current_player]
            )

            if self.check_winner():
                messagebox.showinfo("Победа!", f"Игрок {self.current_player} победил!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Ничья!", "Игра окончена вничью!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

                for button in self.buttons:
                    button.config(bg="#FFB6C1" if self.current_player == "X" else "lightblue")

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " "):
                for i in combo:
                    self.buttons[i].config(bg="lightgreen")
                return True
        return False

    def reset_game(self):
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ", fg="black", bg="SystemButtonFace")
        for button in self.buttons:
            button.config(bg="#FFB6C1")


# Создаем и запускаем игру
root = tk.Tk()
game = TicTacToe(root)
for button in game.buttons:
    button.config(bg="#FFB6C1")
root.mainloop()
