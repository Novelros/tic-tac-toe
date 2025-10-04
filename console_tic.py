class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [" " for _ in range(9)]

    def print_board(self):
        """Вывод игрового поля в консоль"""
        print("\n   |   |   ")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("   |   |   \n")

    def make_move(self, position):
        """Сделать ход"""
        if 1 <= position <= 9 and self.board[position - 1] == " ":
            self.board[position - 1] = self.current_player
            # Смена игрока
            self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False

    def check_winner(self):
        """Проверка победителя"""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # горизонтали
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # вертикали
            [0, 4, 8], [2, 4, 6]  # диагонали
        ]

        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] ==
                    self.board[combo[2]] != " "):
                return True
        return False

    def is_board_full(self):
        """Проверка на ничью"""
        return " " not in self.board

    def play_game(self):
        """Основной игровой цикл"""
        print("Добро пожаловать в Крестики-нолики!")
        print("Для хода введите число от 1 до 9:")
        print(" 1 | 2 | 3 ")
        print("___|___|___")
        print(" 4 | 5 | 6 ")
        print("___|___|___")
        print(" 7 | 8 | 9 ")

        while True:
            self.print_board()

            try:
                position = int(input(f"Ход игрока {self.current_player}: "))
            except ValueError:
                print("Пожалуйста, введите число от 1 до 9!")
                continue

            if not self.make_move(position):
                print("Неверный ход! Попробуйте еще раз.")
                continue

            if self.check_winner():
                self.print_board()
                print(f"Игрок {self.current_player} победил!")
                break
            elif self.is_board_full():
                self.print_board()
                print("Ничья!")
                break


# Запуск игры
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()