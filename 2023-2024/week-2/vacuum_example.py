import time
import threading
from vacuum_board.vacuum import board, get_board, set_board, get_random_board, move_to, get_dirt_pos, get_vacuum_pos




# we will this function for test
# set_board(get_random_board())

set_board([4, 33, [3,2,7,9,22]])

board_thread = threading.Thread(target=board)

board_thread.start()

move_number = 0

moves = ['right', 'bottom', 'left', 'top']

time.sleep(2)  # give some time for GUI startup and initialization

print(get_board())
print(get_vacuum_pos())
print(get_dirt_pos())

while True:
    time.sleep(0.5)
    if not board_thread.is_alive():
        quit()

    move_to(moves[move_number%4])
    move_number = move_number + 1
    print(get_board())
