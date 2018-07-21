import logging
import os
import random

# log levels are: critical, error, warning, info, debug and notset
logging.basicConfig(filename='game.log', level=logging.DEBUG)

CELLS = [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') 


def get_locations():
    return random.sample(CELLS, 3)


def move_player(player, move):
    x, y = player
    if move == 'LEFT':
        x -= 1
    elif move == 'RIGHT':
        x += 1
    elif move == 'UP':
        y += 1
    elif move == 'DOWN':
        y -= 1
    return x, y

def get_moves(player_position):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    # unpacking the tuple
    x, y = player_position
    if x == 0:
        moves.remove('LEFT')
    elif x == 4:
        moves.remove('RIGHT')
    if y == 0:
        moves.remove('DOWN')
    elif y == 4:
        moves.remove('UP')
    return moves


def start_game():
    print("Welcome to the Dugeon")
    input("Press return to start")
    print("Enter QUIT to quit")


def draw_map(player):
    print(" _" * 5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        # the print function takes an argument called end, that tells us what to put at the end of whatever it has printed out. By default it prints out a new line
        print(output, end=line_end)


def game_loop():
    # unpacking the locations
    player, door, monster = get_locations()
    logging.info('player: {}, door: {}, monster: {}'.format(
        player, door, monster))
    playing = True

    while playing:
        clear_screen()
        draw_map(player)
        possible_moves = ", ".join(get_moves(player))
        print("You are currently in the position {}".format(player)) 
        print("You can move {}".format(possible_moves))
        move = input("> ").upper()
        if move == 'QUIT':
            break
        elif move in possible_moves:
            player = move_player(player, move)
            if player == door:
                print("Congratulations, you found the door!")
                playing = False
            elif player == monster:
                print("Oh no, you ran into the monster : (")
                playing = False
        else:
            input("You can't move {}. Please choose one of these moves: {}".format(move, possible_moves))
    else:
        if input("Would you like to play again? [Y/N] ").upper() != 'N':
            game_loop()


clear_screen()
start_game()
game_loop()