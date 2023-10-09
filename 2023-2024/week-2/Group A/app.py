import random
import tkinter
from board import EightPuzzleGUI  # Make sure you have the 'EightPuzzleGUI' class defined in 'board.py'

FILE_PATH="2023-2024\week-2\Group A\solution.txt"


class PuzzleState:
    GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def __init__(self, puzzle, parent=None, move=""):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __hash__(self):
        return hash(str(self.puzzle))

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.puzzle])

    def is_goal(self):
        return self.puzzle == self.GOAL_STATE

    def get_blank_position(self):
        for i in range(3):
            for j in range(3):
                if self.puzzle[i][j] == 0:
                    return i, j

    def get_moves(self):
        i, j = self.get_blank_position()
        moves = []

        if i > 0:
            moves.append("Up")
        if i < 2:
            moves.append("Down")
        if j > 0:
            moves.append("Left")
        if j < 2:
            moves.append("Right")

        return moves

    def expand_state(self, move):
        i, j = self.get_blank_position()
        new_puzzle = [list(row) for row in self.puzzle]

        if move == "Up":
            new_puzzle[i][j], new_puzzle[i - 1][j] = new_puzzle[i - 1][j], new_puzzle[i][j]
        elif move == "Down":
            new_puzzle[i][j], new_puzzle[i + 1][j] = new_puzzle[i + 1][j], new_puzzle[i][j]
        elif move == "Left":
            new_puzzle[i][j], new_puzzle[i][j - 1] = new_puzzle[i][j - 1], new_puzzle[i][j]
        elif move == "Right":
            new_puzzle[i][j], new_puzzle[i][j + 1] = new_puzzle[i][j + 1], new_puzzle[i][j]

        return PuzzleState(new_puzzle, parent=self, move=move)


def dfs_search(initial_state, initial_depth_limit=5):
    while initial_depth_limit <= 100:
        stack = [(initial_state, 0)]  # Store state(node) and depth as a tuple
        visited = set()
        depth_limit = initial_depth_limit

        while stack:
            current_state, depth = stack.pop()
            visited.add(current_state)

            if current_state.is_goal():
                return current_state

            if depth < depth_limit:  # Check if depth is within the limit
                moves = current_state.get_moves()
                for move in moves:
                    child_state = current_state.expand_state(move)
                    if child_state not in visited:
                        stack.append((child_state, depth + 1))

        # If no solution is found within the current depth limit, increase it
        print(f"Current depth limit {initial_depth_limit}")
        initial_depth_limit += 5

    # If no solution is found within the maximum depth limit, return None
    return None


def save_solution_path_to_file(solution_path, filename,directions):
    solution_path = solution_path[::-1]  # Reverse the order of the path
    try:
        with open(filename, "a") as file:
            step_number = 1  # Initialize step number
            for i in range(len(solution_path)):
                state = solution_path[i]
                direction = directions[i]

                file.write(f"Step {step_number} ({direction}):\n")

                for row in state:
                    row_str = "  ".join(map(str, row))
                    file.write(row_str + "\n")
                file.write("\n")
                step_number += 1

            file.write(f"Cost: {len(solution_path)} steps to reach the goal")

        print(f"Solution path saved to {filename}")
    except Exception as e:
        print(f"Error saving solution path to {filename}: {str(e)}")


def check_solvable(puzzle):
    count_inv = 0

    for i in range(0, 9):
        for j in range(i + 1, 9):
            if puzzle[i] > puzzle[j]:
                if puzzle[j] != 0:
                    count_inv += 1

    return count_inv % 2 == 0


def main():
    numbers = list(range(9))
    random.shuffle(numbers)
    print(numbers)

    three_by_three_array = [numbers[i: i + 3] for i in range(0, len(numbers), 3)]

    initial_state = PuzzleState(three_by_three_array)

    with open(FILE_PATH, "w") as file:
        file.write("Initial board:\n")
        for row in three_by_three_array:
            row_str = "  ".join(map(str, row))
            file.write(row_str + "\n")

    if check_solvable(numbers):
        goal_state = dfs_search(initial_state)

        if goal_state:
            goals_path = []
            directions = []
            print("Solution found!")
            while goal_state.parent:
                goals_path.append(goal_state.puzzle)
                directions.append(goal_state.move)
                goal_state = goal_state.parent

            if __name__ == "__main__":
                root = tkinter.Tk()
                app = EightPuzzleGUI(root, goals_path[::-1])
                root.mainloop()

            directions = directions[::-1]
            save_solution_path_to_file(goals_path, FILE_PATH,directions)
        else:
            print("No solution within the maximum depth limit.")
    else:
        print("This puzzle isn't solvable")
        with open(FILE_PATH, "w") as file:
            file.write("The board isn't solvable:\n")


if __name__ == "__main__":
    main()
