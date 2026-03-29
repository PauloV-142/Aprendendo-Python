class Board:
    def __init__(self, w=40, h=40):
        self.w, self.h = w, h
        self.board = self.new_board()
        self.snake = Snake((2, 0), (1, 0)) # Array of Snakes
        self.food = ... # Array of foods
        self.keyPressed = ""
        
    def new_board(self):
        return [["."] * self.w] * self.h
        
    def render(self):
        # Performance: use strings for empty lines, and lists for used ones.
        # if INDEX out of range:
        #   Game over or reappear in the opposite side
        
        # Get a new board, so the symbols can be drawn
        self.board = self.new_board()
        for sprite in self.snake.body:
            x, y = sprite.pos
            row = self.board[y].copy()
            row[x] = "@"
            self.board[y] = row

    def tick(self):
        """Update the snake recursively.
        Verify if SNAKE HEAD and FOOD
        are touching."""
        #if self.snake.isTouchingFood(self.food):
            #self.snake.grow()
            #self.food.teleport()
        
        self.snake.turn(keys[self.keyPressed])
        print(self.snake.turning)
        self.snake.walk()
        self.render()
        self.keyPressed = ""
        
    def mainloop(self):
        print(a)
        while True:
            time.sleep(0.2)
            print("=" * a.w)
            # Use async/subroutine, so the game doesn't wait for the key
            
            # Listen to Input
            self.keyPressed = get_input()
            self.tick()
            print(self)
        
    def __str__(self):
        "PERFORMANCE find a faster way."
        board = []
        for row in self.board:
            board.append("".join(row))
        return "\n".join(board)