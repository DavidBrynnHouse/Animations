import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(f"assets/Attack (1).png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (10, 10)
        self.attack_sprites = []
        self.current_sprite = 0

        for i in range(9):
            self.attack_sprites.append(pygame.image.load(f"assets/Attack ({i + 1}).png"))

    def update(self):
        self.animate(self.attack_sprites, .2)

    def animate(self, sprite_list, speed):
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += 1 * speed
        else:
            self.current_sprite = 0
        self.image = sprite_list[int(self.current_sprite)]
