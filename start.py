import cv2
import numpy as np

from game import Gameboard

startPage = cv2.imread(".\pics\start.png")
rulePage = cv2.imread(".\pics\\rules.png")
lose = cv2.imread(".\pics\lose.png")
win = cv2.imread(".\pics\win.png")
cv2.imshow("Snake2048", startPage)

page = 0
while True:
    key = cv2.waitKey()
    if page == 0 and key == 114:
        page = 1
        cv2.imshow("Snake2048", rulePage)
    if page == 1 and key == 98:
        page = 0
        cv2.imshow("Snake2048", startPage)
    if key == 99:
        cv2.destroyAllWindows()
        break
    if key == 32:
        result = Gameboard().result
        if result == 0:
            cv2.destroyAllWindows()
            break
        if result == 1:
            cv2.imshow("Snake2048", lose)
            while True:
                k = cv2.waitKey()
                if k == 98:
                    break
        if result == 2:
            cv2.imshow("Snake2048", win)
            while True:
                k = cv2.waitKey()
                if k == 98:
                    break
        cv2.imshow("Snake2048", startPage)

