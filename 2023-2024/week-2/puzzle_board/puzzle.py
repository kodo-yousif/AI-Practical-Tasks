import pygame
import random
from tkinter import *
from puzzle_board.Tiles import Tiles

GameBoard=[[1,1,1],[1,1,1],[1,1,1]]
emptyTilePosI=0 
emptyTilePosJ=0

puzzle = [['1', '2', '3'], ['0', '5', '6'], ['4', '7', '8']]


def get_random_puzzle():
	numbers = list(range(9))
	random.shuffle(numbers)
	array_3x3 = [numbers[i:i+3] for i in range(0, 9, 3)]
	return array_3x3

def init_puzzle(new_puzzle = [['1', '2', '3'], ['0', '5', '6'], ['4', '7', '8']]):
	global puzzle
	puzzle = new_puzzle

def board():
	global GameBoard, emptyTilePosI,emptyTilePosJ, puzzle
	pygame.init()

	white=(255,255,255)

	row = 3 
	col = 3

	tilePosX=10
	tilePosY=10

	
	for i in range(row):	
		for j in range(col):
			if int(puzzle[i][j]) == 0: 
					emptyTilePosI=i 
					emptyTilePosJ=j
			GameBoard[i][j]=Tiles(int(puzzle[i][j]),tilePosX,tilePosY)
			tilePosX+=200
		tilePosX=10
		tilePosY+=200 

	tilePosX=10
	tilePosY=10


	gameDisplay=pygame.display.set_mode((595,595))
	pygame.display.set_caption('8-Puzzle') 

	clock = pygame.time.Clock()

	gameExit=False
	

	while not gameExit: 
		
		gameDisplay.fill(white)


		for event in pygame.event.get():	

			if event.type == pygame.QUIT: 
				gameExit=True
				pygame.quit()
				quit()


		for i in range(row):
			for j in range(col):
				gameDisplay.blit(GameBoard[i][j].image,(GameBoard[i][j].xPos,GameBoard[i][j].yPos)) 

		pygame.display.update()

		clock.tick(30); 


def swapTiles(i,j):
	global GameBoard, emptyTilePosI,emptyTilePosJ


	if i not in [0, 1, 2] or j not in [0, 1, 2]:
		print("Error: Invalid tile coordinates.")
		return get_board()
	
	distance = abs(i - emptyTilePosI) + abs(j - emptyTilePosJ)

	if distance == 1:
		GameBoard = GameBoard[i][j].swapTiles(GameBoard,emptyTilePosI, emptyTilePosJ,i,j)
		emptyTilePosI = i
		emptyTilePosJ = j
	else:
		print("Error: The tiles are not neighbors and cannot be swapped.")

	return get_board()

def get_board():
	global GameBoard
	array_3x3 = [[0 for _ in range(3)] for _ in range(3)]


	for i in range(3):
		for j in range(3):
			array_3x3[i][j] = GameBoard[i][j].number
    
	return array_3x3