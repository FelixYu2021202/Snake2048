import numpy as np

from game import Gameboard, BLOCKNAME, imshow, imread, waitKey, destroyWindow, putText

startPage = imread(".\pics\start.png")
rulePage = imread(".\pics\\rules.png")
losebase = imread(".\pics\lose.png")
winbase = imread(".\pics\win.png")
imshow("Snake2048", startPage)

page = 0
while True:
    key = waitKey()
    if page == 0 and key == 114:
        page = 1
        imshow("Snake2048", rulePage)
    if page == 1 and key == 98:
        page = 0
        imshow("Snake2048", startPage)
    if key == 99:
        destroyWindow("Snake2048")
        break
    if key == 32:
        gb = Gameboard()
        result = gb.result
        if result == 1:
            lose = np.array(losebase)
            putText(
                lose,
                "Your score is " + BLOCKNAME[gb.snake[1, 2]],
                (120, 720),
                18,
                3,
                (190, 190, 190),
                4,
            )
            imshow("Snake2048", lose)
        if result == 2:
            win = np.array(winbase)
            imshow("Snake2048", win)
        while True:
            k = waitKey()
            if k == 98:
                break
        imshow("Snake2048", startPage)

