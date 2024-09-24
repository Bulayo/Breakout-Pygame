from settings import *

class Brick(pygame.sprite.Sprite):

    def __init__(self, groups: pygame.sprite.Group, pos: tuple[int], image: pygame.surface.Surface):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_frect(topleft = pos)

    def update(self):
        ...