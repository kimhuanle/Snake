class Snake:
    def __init__(self,x,y,xlim,ylim,xd,yd):
        self.x = x                      # Position of head
        self.y = y
        self.xlim = xlim            # Borders
        self.ylim = ylim
        self.xd = xd                  # Direction
        self.yd = yd
        self.body = [(x-1,y),(x-0.5,y),(x,y)]         # Body of snake
        self.moveQueue = []
        self.len = 3                  # Snake's length

    def update(self, x, y):        # x, y are coordinates of cherry
        self.x += self.xd            # Update head's position
        self.y += self.yd
        
        if self.x > self.xlim:        # Wrap around at borders
            self.x = 0
        if self.x < 0:
            self.x =self. xlim
        if self.y > self.ylim:
            self.y = 0
        if self.y < 0:
            self.y =self. ylim

        check = self.x == x and self.y == y
        if check:
            self.len += 1
   
        self.body.append((self.x, self.y))
        if len(self.body) > self.len:
            del self.body[0]

        if (self.x/0.5) % 2 == 0 and (self.y/0.5) % 2 == 0 and len(self.moveQueue) > 0:
            if self.moveQueue[-1] == 'up':
                self.xd = 0
                self.yd = -0.5
                del self.moveQueue[-1]
            elif self.moveQueue[-1] == 'down':
                self.xd = 0
                self.yd = 0.5
                del self.moveQueue[-1]
            elif self.moveQueue[-1] == 'left':
                self.xd = -0.5
                self.yd = 0
                del self.moveQueue[-1]
            elif self.moveQueue[-1] == 'right':
                self.xd = 0.5
                self.yd = 0
                del self.moveQueue[-1]

        if check:
            return True

    def check(self):
        for a in self.body[:-1]:
            if a[0] == self.x and a[1] == self.y:
                return True
        return False