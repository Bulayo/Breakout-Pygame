from settings import *
from random import choice

class Ball(pygame.sprite.Sprite):
    
    def __init__(self, groups: pygame.sprite.Group, pos: tuple[int], image: pygame.surface.Surface, collision_sprites: pygame.rect.Rect):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_frect(center = pos)
        self.direction = pygame.Vector2(choice([1, -1]), choice([1, -1]))
        self.speed = 200
        self.collision_sprites = collision_sprites


    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.collision("horizontal")
        self.rect.y += self.direction.y * self.speed * dt
        self.collision("verticle")

        if self.rect.right <= 0 or self.rect.left >= WIDTH:
            self.direction.x = -self.direction.x

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.direction.y = -self.direction.y
            
        if self.direction == 0:
            self.direction.normalize()

        else:
            self.direction = self.direction

    def collision(self, direction):
        for sprite in self.collision_sprites:
            for collision_rect in sprite:
                if collision_rect.rect.colliderect(self.rect):
                    if direction == "horizontal":
                        if self.direction.x > 0:
                            self.direction.x = -self.direction.x

                        if self.direction.x < 0:
                            self.direction.x = -self.direction.x

                    if direction == "verticle":
                        if self.direction.y > 0:
                            self.direction.y = -self.direction.y

                        if self.direction.y < 0:
                            self.direction.y = -self.direction.y
