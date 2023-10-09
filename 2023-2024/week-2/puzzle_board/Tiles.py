import os
import pygame


class Tiles:
    def __init__(self, number, xPos, yPos):
        self.number = number
        self.xPos = xPos
        self.yPos = yPos

        assets_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
        image_path = os.path.join(assets_path, f"{self.number}.png")

        self.image = pygame.image.load(image_path)

        self.image = pygame.transform.scale(self.image, (175, 175))

        self.rectangle = self.image.get_rect()
        self.rectangle.center = (xPos + 87.5, yPos + 87.5)

    def swapTiles(
        self, GameBoard, emptyTilePosI, emptyTilePosJ, i, j
    ):  # if you the tile is being swapped
        temporaryX = GameBoard[emptyTilePosI][
            emptyTilePosJ
        ].xPos  # get the temporary position of the empty tile in the gui and the gameboard
        temporaryY = GameBoard[emptyTilePosI][emptyTilePosJ].yPos
        GameBoard[emptyTilePosI][emptyTilePosJ].xPos = GameBoard[i][
            j
        ].xPos  # switch their positions (coordinates in GUI and position in array)
        GameBoard[emptyTilePosI][emptyTilePosJ].yPos = GameBoard[i][j].yPos
        GameBoard[i][j].xPos = temporaryX
        GameBoard[i][j].yPos = temporaryY

        GameBoard[i][j].setRectangle()
        # set the rectangle of the image again of the tile switched

        GameBoard[emptyTilePosI][emptyTilePosJ].setRectangle()
        # set the rectangle of the empty tile

        GameBoard[i][j], GameBoard[emptyTilePosI][emptyTilePosJ] = (
            GameBoard[emptyTilePosI][emptyTilePosJ],
            GameBoard[i][j],
        )  # switch the position of the tile and empty tile in thje array

        return GameBoard

    def setRectangle(self):  # to set my tile's image rectangle again
        self.rectangle = self.image.get_rect()
        # to not make my rectangle go to 0,0 after creating it for the image
        self.rectangle.center = (self.xPos + 87.5, self.yPos + 87.5)
