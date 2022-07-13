# Snake2048
#### my first python game
by FelixYu2021202:

### How to start:
Run *start.exe* **I compiled my python codes into an executable file**

Or Run *start.py* **This is the source code**

***Notice: If you want to run this game, please download the whole repository! The files are relevant to each other!***

#### How to play:
1. Press `space` twice to start
2. Press `wasd` to change the direction of the snake
3. Make sure the block the snake is `eating` is *smaller than or equal to* the *biggest number in the snake*(the first one) or the snake will crash and died (game over)
4. Don't let the snake crash into the walls
5. Your goal is to let the biggest number on the snake be `1Q` (1 quadrillion)
6. Have fun

_You can watch the video `play.mp4` to know more about this game_



##### Some advices for playing this game
1. Always try to eat the biggest block (that you can) first.
2. If you think the snake is too slow, press a key and don't release it, in the game page, only 'wasd', 'c', escape key ('c' and escape key are for shutting down the game) will change the status, so if you want to speed up, it's recommended to press the key of the current direction or any key except of these three.
3. The probability of generating blocks are in `p.xls`, you can change the probability in `p.xls`. It's safe. The backgrounds of the data are colored in *red, green, yellow, light and dark blue*, other blocks have no use. *The first column shows the biggest number on the snake, the first row shows the number that may be generated in this turn*
4. About three rounds (the snake moves three blocks), it will generate one block on the gameboard, about six rounds it will generate two block on the gameboard. It's better to 'clean up' when there are many small blocks.
