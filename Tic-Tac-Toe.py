board = list(range(1, 10))
winning_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


class View:
    @staticmethod
    def draw_board():
        print('-------------')
        for i in range(3):
            print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-------------')


class Model:
    def take_input(player_choice):
        while True:
            value = input("Where to put: " + player_choice + " ? ")
            if not (value in '123456789'):
                print("Wrong entry. Please repeat")
                continue
            value = int(value)
            if str(board[value - 1]) in 'XO':
                print("This cell is already occupied. Try another")
                continue
            board[value - 1] = player_choice
            break


class Controller:
    @staticmethod
    def check_win():
        for i in winning_combinations:
            if (board[i[0] - 1]) == (board[i[1] - 1]) == (board[i[2] - 1]):
                return board[i[1] - 1]
        else:
            return False


def main():
    counter = 0
    while True:
        View.draw_board()
        if counter % 2 == 0:
            Model.take_input("X")
        else:
            Model.take_input("O")
        if counter > 3:
            winner = Controller.check_win()
            if winner:
                View.draw_board()
                print(winner, "Win!")
                break
        counter += 1
        if counter > 8:
            View.draw_board()
            print("Draw!")


if __name__ == '__main__':
    main()
