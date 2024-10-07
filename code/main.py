from settings import *
from levels import *
from bricks import Brick
from paddle import Paddle
from ball import Ball

class Game:
    
    def __init__(self):
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Breakout")
        self.clock = pygame.time.Clock()
        self.running = True

        # Images
        self.brick_list = [pygame.image.load(join("assets", f"Brick{i}.png")) for i in range(1, 6)]
        self.paddle_img = pygame.image.load(join("assets", "paddle.png"))
        self.ball_img = pygame.image.load(join("assets", "ball.png"))

        # Groups
        self.brick_group = pygame.sprite.Group()
        self.paddle_group = pygame.sprite.Group()
        self.ball_group = pygame.sprite.Group()

        # levels
        self.levels = {1: level_1}
        self.current_level = 1

        # Objects
        self.player = Paddle(self.paddle_group, (WIDTH / 2, 470), self.paddle_img)


    def run(self):

        while self.running:
            self.WIN.fill((50, 50, 50))
            self.dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Update
            self.load_level()
            self.brick_group.update()
            self.paddle_group.update(self.dt)
            self.ball_group.update(self.dt)

            # Draw
            self.brick_group.draw(self.WIN)
            self.paddle_group.draw(self.WIN)
            self.ball_group.draw(self.WIN)

            pygame.display.flip()


        pygame.quit()


    def load_level(self):
        if len(self.brick_group) < 1 + len(self.levels[self.current_level]): 
            self.row = 1
            for row in self.levels[self.current_level]:
                self.column = 1
                for tile in row:
                    if tile == 1:
                        Brick(self.brick_group, (self.column * 60, self.row * 40), self.brick_list[0])

                    elif tile == 2:
                        Brick(self.brick_group, (self.column * 60, self.row * 40), self.brick_list[1])

                    elif tile == 3:
                        Brick(self.brick_group, (self.column * 60, self.row * 40), self.brick_list[2])

                    elif tile == 4:
                        Brick(self.brick_group, (self.column * 60, self.row * 40), self.brick_list[3])

                    elif tile == 5:
                        Brick(self.brick_group, (self.column * 60, self.row * 40), self.brick_list[4])

                    elif tile == 6:
                        Ball(self.ball_group, (WIDTH / 2, 400), self.ball_img, (self.brick_group, self.paddle_group))
                        

                    self.column += 1
                self.row += 1


if __name__ == "__main__":
    game = Game()
    game.run()