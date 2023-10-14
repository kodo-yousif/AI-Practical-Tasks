import sys

sys.path.append("2023-2024\week-2\puzzle_board")

import random
import heapq
import tkinter as tk
from tkinter import messagebox


# Define the goal state
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Function to check if two puzzle states are equal
def is_goal_state(state):
    return state == goal_state
[[],[],[]]

# Function to calculate the heuristic (Manhattan distance) for the puzzle
def heuristic(state):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i * 3 + j] != 0:
                target_i, target_j = divmod(state[i * 3 + j] - 1, 3)
                h += abs(i - target_i) + abs(j - target_j)
    return h


# Function to get valid neighbor states for a given state
def get_neighbors(state):
    neighbors = []

    empty_index = state.index(0)
    row, col = divmod(empty_index, 3)

    # Possible moves: left, right, up, down
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            neighbor_state = state[:]
            neighbor_index = new_row * 3 + new_col
            neighbor_state[empty_index], neighbor_state[neighbor_index] = (
                neighbor_state[neighbor_index],
                neighbor_state[empty_index],
            )
            neighbors.append(neighbor_state)

    return neighbors


# Function to perform Best-First Search
def best_first_search(initial_state):
    frontier = []  # Use a list for a priority queue
    visited = set()
    parent = {}
    cost = {}

    def custom_comparator(state):
        return heuristic(state)

    heapq.heappush(frontier, (custom_comparator(initial_state), initial_state))

    visited.add(tuple(initial_state))
    cost[tuple(initial_state)] = 0

    while frontier:
        priority, current_state = heapq.heappop(frontier)

        if is_goal_state(current_state):
            path = []
            while current_state != initial_state:
                path.append(current_state)
                current_state = parent[tuple(current_state)]
            path.append(initial_state)
            path.reverse()
            return path

        for neighbor_state in get_neighbors(current_state):
            if tuple(neighbor_state) not in visited:
                heapq.heappush(
                    frontier, (custom_comparator(neighbor_state), neighbor_state)
                )
                visited.add(tuple(neighbor_state))
                parent[tuple(neighbor_state)] = current_state
                cost[tuple(neighbor_state)] = cost[tuple(current_state)] + 1

    return None


def save_solution_to_file(initial_state, solution_path):
    with open("2023-2024\week-2\Group D - 8-puzzle best FS\solution.txt", "w") as file:
        file.write("Initial Puzzle Board:\n")
        for i in range(0, 9, 3):
            file.write(" ".join(map(str, initial_state[i : i + 3])) + "\n")

        if solution_path:
            file.write("\nSteps to Solution:\n")
            for step, state in enumerate(solution_path):
                file.write(f"Step {step + 1}:\n")
                for i in range(0, 9, 3):
                    file.write(" ".join(map(str, state[i : i + 3])) + "\n")
            file.write(
                "\nOverall Cost of Solution: {}\n".format(len(solution_path) - 1)
            )
        else:
            file.write("\nNot Solvable!")
            messagebox.showerror("No Solution", "The puzzle is not solvable!")


# Create a Tkinter window for displaying the solution steps
solution_root = tk.Tk()
solution_root.title("8-Puzzle Solution Viewer")


def generate_random_puzzle():
    numbers = list(range(9))
    random.shuffle(numbers)
    return numbers


# Create the puzzle board
initial_state = generate_random_puzzle()
buttons = []
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = tk.Button(solution_root, text="", width=10, height=4)
        button.grid(row=i, column=j)
        row_buttons.append(button)
    buttons.append(row_buttons)


# Function to update the puzzle board
def update_board():
    for i in range(3):
        for j in range(3):
            num = initial_state[i * 3 + j]
            buttons[i][j].config(
                text=str(num) if num != 0 else "",
                state=tk.DISABLED if num == 0 else tk.NORMAL,
            )


# Function to auto-update the puzzle board
def auto_update_board():
    global step_index
    if step_index < len(solution_steps):
        initial_state[:] = solution_steps[step_index]
        update_board()
        step_index += 1
        solution_root.after(
            100, auto_update_board
        )  # Schedule the next update after 0.1 second
    else:
        messagebox.showinfo("Solution Completed", "Puzzle is already solved!")


update_board()

# Display the solution steps
solution_steps = best_first_search(initial_state)
save_solution_to_file(initial_state, solution_steps)
step_index = 0

# Start the auto-update process
auto_update_board()

# Start the Tkinter main loop for the solution viewer
solution_root.mainloop()
