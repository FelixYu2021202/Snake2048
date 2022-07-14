#### *There are some things that you **CAN CHANGE** about this game:*
1. The speed of the snake: in `game.py`, *line 83*, `SETTINGS["speed"]`, the default is `60`, `type(int)`.
2. The starting biggest number of the snake: in `game.py`, *line 83*, `SETTINGS["start"]`, the default is `"2"`, `type(str)`.
3. The (reciprocals of the) probability of whether or not to generate ***one*** block in this round: in `game.py`, *line 83*, `SETTINGS["generate.one"]`, the default is `3`, `type(int)`.
4. The (reciprocals of the) probability of whether or not to generate ***two*** block in this round: in `game.py`, *line 83*, `SETTINGS["generate.two"]`, the default is `6`, `type(int)`.
5. The probability of generating blocks: in `p.xls`. The backgrounds of the data are colored in *red, green, yellow, light and dark blue*, other blocks have no use. *The first column shows the biggest number on the snake, the first row shows the number that may be generated in this turn*.
