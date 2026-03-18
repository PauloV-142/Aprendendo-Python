Architecture:

Snake & Sprite should be subclasses of Board, so they exchange data properly.

For rendering:
(this is why the Architecture needs change)

When a sprite changes position:
Save it's **earlier** position on e.g. board.erase list.
Save it's **new** position on e.g. board.draw list.

On each board.tick() *draw* the positions in board.draw, and *erase* the positions in board.erase.

*Draw* is change an empty character to a painted one (`'.' -> '@'`).
Erasing is the inverse: (`'@' -> '.'`).


For game starting:
```py
b = Board(w, h, configs={...})

# Or:
b.configs(foods, wallBehavior, players, level, difficultyIncrease)

b.createSnake((x, y), (x, y))

b.mainLoop()
```
