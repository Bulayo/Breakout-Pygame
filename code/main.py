from settings import *

class Game:
    
    def __init__(self):
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Breakout")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):

        while self.running:
            self.WIN.fill((50, 50, 50))
            self.dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()

        pygame.quit()
                    

if __name__ == "__main__":
    game = Game()
    game.run()