import time
import threading
import puzzle_board.puzzle as pz
import puzzle_board.Tiles as t


# we will this function for test
# init_puzzle(get_random_puzzle())

pz.init_puzzle([["1", "2", "3"], ["0", "5", "6"], ["4", "7", "8"]])

board_thread = threading.Thread(target=pz.board)


board_thread.start()


is_moved = True


time.sleep(2)  # give some time for GUI startup and initialization

print(pz.get_board())

while True:
    time.sleep(2)
    if not board_thread.is_alive():
        quit()

    if is_moved:
        board_array = pz.swapTiles(1, 1)
    else:
        board_array = pz.swapTiles(1, 0)

    print(board_array)
    is_moved = not is_moved
