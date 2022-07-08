import cv2
import numpy as np
from random import randint
from probability import PROBABILITY


def P_randint(probability):
    s = probability[49]
    # p = [int(x) for x in probability]
    rand = randint(1, s)
    for x in range(50):
        if rand <= probability[x]:
            return x + 1


S = -1

blockname = """
2
4
8
16
32
64
128
256
512
1024
2048
4096
8192
16K
32K
65K
131K
262K
524K
1M
2M
4M
8M
16M
33M
67M
134M
268M
536M
1B
2B
4B
8B
17B
34B
68B
137B
274B
549B
1T
2T
4T
8T
17T
35T
70T
140T
281T
562T
1Q
""".split(
    "\n"
)
blockbase = cv2.imread(".\pics\\block.b.png")
picsB = [cv2.imread(".\pics\\b" + x + ".b.png") for x in blockname]  # blocks
picsS = [cv2.imread(".\pics\\s" + x + ".b.png") for x in blockname]  # snake's'
snakeheadbase = cv2.imread(".\pics\shead.b.png")
snakehead = [
    np.rot90(snakeheadbase, k=3),
    snakeheadbase,
    np.rot90(snakeheadbase),
    np.rot90(snakeheadbase, k=2),
]


class Gameboard:
    gameboardbase = np.ones((960, 960, 3), np.uint8)
    gameboard = np.array([])
    gameboarddat = np.array([])
    snake = np.zeros((64, 4), np.int32)
    nextdir = -1
    biggest = 1
    cur = 0
    status = 1  # 1: alive, 0: died
    length = 2

    def __init__(self):
        for i in range(0, 920, 120):
            for j in range(0, 920, 120):
                self.gameboardbase[i : i + 120, j : j + 120] = blockbase
                self.gameboarddat = np.array(
                    [
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, S, S, S, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                    ]
                )
        cv2.imshow("game", self.gameboardbase)
        while True:
            key = cv2.waitKey()
            if key == 32:
                self.startGame()
                break
            if key == 99:
                cv2.destroyAllWindows()
                break

    def startGame(self):
        self.snake = np.full((64, 4), -2, np.int32)
        self.snake[0] = [
            3,  # x
            4,  # y
            -1,  # -2: nothing, -1: head, 1~50: number
            0,  # 0: left, 1: up, 2: right, 3: down
        ]
        self.snake[1] = [3, 5, 1, 0]
        self.length = 2
        self.biggest = 1
        x, y = self.getpos()
        num = self.getnum()
        self.gameboarddat[x, y] = num
        x, y = self.getpos()
        num = self.getnum()
        self.gameboarddat[x, y] = num
        st = self.render()
        if st == 0:  # key 'c': shut down the whole game
            return
        # snake # no need to eat right now
        ## move & eat
        ### eat (no need)
        ### move
        for i in range(8):
            for j in range(8):
                if self.gameboarddat[i, j] == S:
                    self.gameboarddat[i, j] = 0
        for i in range(self.length):
            if self.snake[i, 3] == 0:
                self.snake[i, 1] -= 1
            if self.snake[i, 3] == 1:
                self.snake[i, 0] -= 1
            if self.snake[i, 3] == 2:
                self.snake[i, 1] += 1
            if self.snake[i, 3] == 3:
                self.snake[i, 0] += 1
            self.gameboarddat[self.snake[i, 0], self.snake[i, 1]] = S
        for i in range(self.length - 1, 0, -1):
            self.snake[i, 3] = self.snake[i - 1, 3]
        hd = self.snake[0, 3]
        if hd == 0:
            if self.snake[0, 1] > 0:
                if self.gameboarddat[self.snake[0, 0], self.snake[0, 1] - 1] == 0:
                    self.gameboarddat[self.snake[0, 0], self.snake[0, 1] - 1] = S
        if hd == 1:
            if self.snake[0, 0] > 0:
                if self.gameboarddat[self.snake[0, 0] - 1, self.snake[0, 1]] == 0:
                    self.gameboarddat[self.snake[0, 0] - 1, self.snake[0, 1]] = S
        if hd == 2:
            if self.snake[0, 1] < 7:
                if self.gameboarddat[self.snake[0, 0], self.snake[0, 1] + 1] == 0:
                    self.gameboarddat[self.snake[0, 0], self.snake[0, 1] + 1] = S
        if hd == 3:
            if self.snake[0, 0] < 7:
                if self.gameboardat[self.snake[0, 0] + 1, self.snake[0, 1]] == 0:
                    self.gameboarddat[self.snake[0, 0] + 1, self.snake[0, 1]] = S
        if self.nextdir > -1:  # change the direction of the head
            self.snake[0, 3] = self.nextdir
            self.nextdir = -1

        while self.status:
            # block
            if randint(1, 3) == 1:  # 0.3333 chance
                x, y = self.getpos()
                num = self.getnum()
                self.gameboarddat[x, y] = num
            if randint(1, 5) == 1:  # 0.2 chance
                x, y = self.getpos()
                num = self.getnum()
                self.gameboarddat[x, y] = num
            ## crashed
            hd = self.snake[0, 3]
            if hd == 0:
                if self.snake[0, 1] == 0:  # crashed into a wall
                    self.status = 0
                    break
                if (
                    self.gameboarddat[self.snake[0, 0], self.snake[0, 1] - 1]
                    > self.biggest
                    # or self.gameboarddat[self.snake[0, 0], self.snake[0, 1] - 1] < 0
                ):  # crashed into a bigger block or itself
                    self.status = 0
                    break
            if hd == 1:
                if self.snake[0, 0] == 0:
                    self.status = 0
                    break
                if (
                    self.gameboarddat[self.snake[0, 0] - 1, self.snake[0, 1]]
                    > self.biggest
                    # or self.gameboarddat[self.snake[0, 0] - 1, self.snake[0, 1]] < 0
                ):
                    self.status = 0
                    break
            if hd == 2:
                if self.snake[0, 1] == 7:
                    self.status = 0
                    break
                if (
                    self.gameboarddat[self.snake[0, 0], self.snake[0, 1] + 1]
                    > self.biggest
                    # or self.gameboarddat[self.snake[0, 0], self.snake[0, 1] + 1] < 0
                ):
                    self.status = 0
                    break
            if hd == 3:
                if self.snake[0, 0] == 7:
                    self.status = 0
                    break
                if (
                    self.gameboarddat[self.snake[0, 0] + 1, self.snake[0, 1]]
                    > self.biggest
                    # or self.gameboarddat[self.snake[0, 0] + 1, self.snake[0, 1]] < 0
                ):
                    self.status = 0
                    break
            st = self.render()
            if st == 0:  # key 'c': shut down the whole game
                return
            if self.biggest == 50:
                print("you win!")  # TODO: alert
                return
            # snake
            ## move & eat
            ### eat
            x, y = self.snake[0, 0:2]
            if hd == 0:
                y -= 1
            if hd == 1:
                x -= 1
            if hd == 2:
                y += 1
            if hd == 3:
                x += 1
            if self.gameboarddat[x, y] > 0:
                newnum = self.gameboarddat[x, y]
                self.gameboarddat[x, y] = S
                #### merge
                merge = 0
                for i in range(1, self.length):
                    if self.snake[i, 2] == newnum:
                        pos = i
                        newnum += 1
                        pos -= 1
                        while pos > 0 and self.snake[pos, 2] == newnum:
                            newnum += 1
                            pos -= 1
                        pos += 1
                        self.snake[pos, 2] = newnum
                        self.biggest = max(newnum, self.biggest)
                        pl = i - pos
                        for j in range(i + 1, self.length):
                            self.snake[j - pl, 2] = self.snake[j, 2]
                        self.length -= pl
                        merge = 1
                        break
                #### *add
                if not merge:
                    pos = self.length
                    for i in range(1, self.length):
                        if self.snake[i, 2] < newnum:
                            pos = i
                            break
                    for i in range(self.length, pos, -1):
                        self.snake[i, 2] = self.snake[i - 1, 2]
                    self.snake[pos, 2] = newnum
                    self.snake[self.length, 0] = self.snake[self.length - 1, 0]
                    self.snake[self.length, 1] = self.snake[self.length - 1, 1] + 1
                    self.snake[self.length, 3] = 0
                    self.length += 1

            ### move
            for i in range(8):
                for j in range(8):
                    if self.gameboarddat[i, j] == S:
                        self.gameboarddat[i, j] = 0
            for i in range(self.length):
                if self.snake[i, 3] == 0:
                    self.snake[i, 1] -= 1
                if self.snake[i, 3] == 1:
                    self.snake[i, 0] -= 1
                if self.snake[i, 3] == 2:
                    self.snake[i, 1] += 1
                if self.snake[i, 3] == 3:
                    self.snake[i, 0] += 1
                self.gameboarddat[self.snake[i, 0], self.snake[i, 1]] = S
            for i in range(self.length - 1, 0, -1):
                self.snake[i, 3] = self.snake[i - 1, 3]
            for i in range(8):
                for j in range(8):
                    if self.gameboarddat[i, j] == S:
                        self.gameboarddat[i, j] = 0
            if hd == 0:
                if self.snake[0, 1] > 0:
                    if self.gameboarddat[self.snake[0, 0], self.snake[0, 1] - 1] == 0:
                        self.gameboarddat[self.snake[0, 0], self.snake[0, 1] - 1] = S
            if hd == 1:
                if self.snake[0, 0] > 0:
                    if self.gameboarddat[self.snake[0, 0] - 1, self.snake[0, 1]] == 0:
                        self.gameboarddat[self.snake[0, 0] - 1, self.snake[0, 1]] = S
            if hd == 2:
                if self.snake[0, 1] < 7:
                    if self.gameboarddat[self.snake[0, 0], self.snake[0, 1] + 1] == 0:
                        self.gameboarddat[self.snake[0, 0], self.snake[0, 1] + 1] = S
            if hd == 3:
                if self.snake[0, 0] < 7:
                    if self.gameboarddat[self.snake[0, 0] + 1, self.snake[0, 1]] == 0:
                        self.gameboarddat[self.snake[0, 0] + 1, self.snake[0, 1]] = S
            if self.nextdir > -1:  # change the direction of the head
                self.snake[0, 3] = self.nextdir
                hd = self.snake[0, 3]
                self.nextdir = -1

        print("you died")  # TODO: alert

    def render(self):
        self.cur = 0
        while self.cur < 24:  # 24 fps
            self.gameboard = np.array(self.gameboardbase)
            for x in range(8):  # render board
                for y in range(8):
                    if self.gameboarddat[x, y] > 0:
                        num = self.gameboarddat[x, y]
                        self.gameboard[
                            x * 120 : x * 120 + 120, y * 120 : y * 120 + 120
                        ] = picsB[num]

            for i in range(self.length):
                x, y, t, d = self.snake[i]
                if d == 1:
                    if t == -1:
                        self.gameboard[
                            x * 120
                            + 22
                            - self.cur * 5 : x * 120
                            + 120
                            - 23
                            - self.cur * 5,
                            y * 120 + 22 : y * 120 + 120 - 23,
                        ] = snakehead[0]
                    else:
                        self.gameboard[
                            x * 120
                            + 22
                            - self.cur * 5 : x * 120
                            + 120
                            - 23
                            - self.cur * 5,
                            y * 120 + 22 : y * 120 + 120 - 23,
                        ] = picsS[t]
                if d == 0:
                    if t == -1:
                        self.gameboard[
                            x * 120 + 22 : x * 120 + 120 - 23,
                            y * 120
                            + 22
                            - self.cur * 5 : y * 120
                            + 120
                            - 23
                            - self.cur * 5,
                        ] = snakehead[1]
                    else:
                        self.gameboard[
                            x * 120 + 22 : x * 120 + 120 - 23,
                            y * 120
                            + 22
                            - self.cur * 5 : y * 120
                            + 120
                            - 23
                            - self.cur * 5,
                        ] = picsS[t]
                if d == 3:
                    if t == -1:
                        self.gameboard[
                            x * 120
                            + 22
                            + self.cur * 5 : x * 120
                            + 120
                            - 23
                            + self.cur * 5,
                            y * 120 + 22 : y * 120 + 120 - 23,
                        ] = snakehead[2]
                    else:
                        self.gameboard[
                            x * 120
                            + 22
                            + self.cur * 5 : x * 120
                            + 120
                            - 23
                            + self.cur * 5,
                            y * 120 + 22 : y * 120 + 120 - 23,
                        ] = picsS[t]
                if d == 2:
                    if t == -1:
                        self.gameboard[
                            x * 120 + 22 : x * 120 + 120 - 23,
                            y * 120
                            + 22
                            + self.cur * 5 : y * 120
                            + 120
                            - 23
                            + self.cur * 5,
                        ] = snakehead[3]
                    else:
                        self.gameboard[
                            x * 120 + 22 : x * 120 + 120 - 23,
                            y * 120
                            + 22
                            + self.cur * 5 : y * 120
                            + 120
                            - 23
                            + self.cur * 5,
                        ] = picsS[t]
                i += 1

            cv2.imshow("game", self.gameboard)
            key = cv2.waitKey(24)  # 1000/24ms is about 42ms
            if key == 99:
                cv2.destroyAllWindows()
                return 0
            if key == 97:
                print("left")
                self.nextdir = 0
            if key == 119:
                print("up")
                self.nextdir = 1
            if key == 100:
                print("right")
                self.nextdir = 2
            if key == 115:
                print("down")
                self.nextdir = 3
            self.cur += 1
        return 1

    def getpos(self):
        x = randint(0, 7)
        y = randint(0, 7)
        while self.gameboarddat[x, y] != 0:
            x = randint(0, 7)
            y = randint(0, 7)
        return x, y

    def getnum(self):
        return P_randint(PROBABILITY[self.biggest])


Gameboard()
