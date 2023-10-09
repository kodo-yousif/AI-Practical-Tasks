import tkinter as tk
from tkinter import PhotoImage
import time


class EightPuzzleGUI:
    def __init__(self, root, solution_path):
        self.root = root
        self.root.title("8 Puzzle Game")
        self.solution = solution_path
        self.current_step = 0

        # Load images for numbers 1 to 8 and blank
        self.images = [
            PhotoImage(file=f"2023-2024/week-2/puzzle_board/assets/{i}.png")
            for i in range(1, 9)
        ]
        self.images.append(
            PhotoImage(file=f"2023-2024/week-2/puzzle_board/assets/0.png")
        )

        # Initialize the puzzle board
        self.puzzle_board = [
            [2, 1, 3],
            [4, 5, 6],
            [7, 8, 9],  # 9 represents the blank space
        ]

        # Create labels for each tile
        self.labels = [[None, None, None], [None, None, None], [None, None, None]]

        for i in range(3):
            for j in range(3):
                tile_number = self.puzzle_board[i][j]
                self.labels[i][j] = tk.Label(root, image=self.images[tile_number - 1])
                self.labels[i][j].grid(row=i, column=j)

        # Schedule the periodic update
        self.update_puzzle()

    def update_puzzle(self):
        if self.current_step < len(self.solution):
            step = self.solution[self.current_step]
            self.update_labels(step)
            self.current_step += 1
            self.root.after(
                150, self.update_puzzle
            )  # Schedule the next update in 1 second

    def update_labels(self, step):
        for i in range(3):
            for j in range(3):
                tile_number = step[i][j]
                self.labels[i][j].config(image=self.images[tile_number - 1])
