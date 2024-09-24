from settings import *
from levels import *
from bricks import Brick

class Game:
    
    def __init__(self):
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Breakout")
        self.clock = pygame.time.Clock()
        self.running = True

        # Images
        self.brick1_image = pygame.image.load(join("assets", "Brick1.png")).convert_alpha()
        self.brick2_image = pygame.image.load(join("assets", "Brick2.png")).convert_alpha()
        self.brick3_image = pygame.image.load(join("assets", "Brick3.png")).convert_alpha()
        self.brick4_image = pygame.image.load(join("assets", "Brick4.png")).convert_alpha()
        self.brick5_image = pygame.image.load(join("assets", "Brick5.png")).convert_alpha()

        # Groups
        self.brick_group = pygame.sprite.Group()

        self.row = 1
        for row in level_1:
            self.column = 1
            for tile in row:
                if tile == 1:
                    Brick(self.brick_group, (self.column * 60, self.row * 40), self.brick1_image)
                
                elif tile == 2:
                    Brick(self.brick_group, (self.column * 60, self.row * 40), self.brick2_image)

                elif tile == 3:
                    Brick(self.brick_group, (self.column * 60, self.row * 40), self.brick3_image)

                elif tile == 4:
                    Brick(self.brick_group, (self.column * 60, self.row * 40), self.brick4_image)

                elif tile == 5:
                    Brick(self.brick_group, (self.column * 60, self.row * 40), self.brick5_image)

                self.column += 1
            self.row += 1


    def run(self):

        while self.running:
            self.WIN.fill((50, 50, 50))
            self.dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Update
            self.brick_group.update()

            # Draw
            self.brick_group.draw(self.WIN)

            pygame.display.flip()

        pygame.quit()
   

if __name__ == "__main__":
    game = Game()
    game.run()