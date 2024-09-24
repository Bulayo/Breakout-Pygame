from settings import *

class Paddle(pygame.sprite.Sprite):

    def __init__(self, groups: pygame.sprite.Group, pos: tuple[int], image: pygame.surface.Surface):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_frect(center = pos)
        self.direction = pygame.Vector2()
        self.speed = 200

    def update(self, delta_time):
        self.input()
        self.move(delta_time)
        self.bounds()

    def input(self):
        keys = pygame.key.get_pressed()

        self.direction.x = (keys[pygame.K_RIGHT] or keys[pygame.K_d]) - (keys[pygame.K_LEFT] or keys[pygame.K_a])

    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt

    def bounds(self):
        if self.rect.left <= 0:
            self.rect.left = 0

        elif self.rect.right >= WIDTH:
            self.rect.right = WIDTH