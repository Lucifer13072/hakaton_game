import random

def get_winner(player1, player2):
    if player1 == player2:
        return "Ничья"

    if (player1 == "камень" and player2 == "ножницы") or (player1 == "ножницы" and player2 == "бумага") or (player1 == "бумага" and player2 == "камень"):
        return "Игрок 1"

    return "Игрок 2"

def get_move():
    moves = {
        "left": "голова",
        "up": "руки",
        "right": "ноги"
    }

    while True:
        key = input("Ваш ход: ")
        if key in moves:
            return moves[key]
        else:
            print("Некорректный ввод. Попробуйте снова.")

def game():
    print("Начинаем игру 'Камень, ножницы, бумага, голова, руки, ноги'!")
    print("Для выбора удара используйте клавиши стрелочек:")
    print("← - голова")
    print("↑ - руки")
    print("→ - ноги")
    print()

    while True:
        player1_move = get_move()
        player2_move = get_move()
        
        print(f"Игрок 1 выбрал: {player1_move}")
        print(f"Игрок 2 выбрал: {player2_move}")
        print()

        winner = get_winner(player1_move, player2_move)
        print(f"Результат: {winner} побеждает!")
        print()

        play_again = input("Хотите сыграть ещё раз? (да/нет): ")
        if play_again.lower() != "да":
            break

game()S
