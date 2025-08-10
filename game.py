import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Platform Game")

        self.clock = pygame.time.Clock()

        self.img = pygame.image.load("data/images/clouds/cloud_1.png")
        self.img.set_colorkey((0, 0, 0))
        self.img_pos = [160, 260]

        self.movement = [False, False] # Booleans chacking if a button is held down

        self.collisions_area = pygame.Rect(50, 50, 300, 50)

    def run(self):
        while True:
            self.screen.fill((14, 219, 248))

            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            if img_r.colliderect(self.collisions_area):
                pygame.draw.rect(self.screen, (0, 100, 255), self.collisions_area)
            else: pygame.draw.rect(self.screen, (0, 50, 255), self.collisions_area)

            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5 # Equates to 5, -5 or 0 based on the keys held down
            self.screen.blit(self.img, self.img_pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False



            pygame.display.update()
            self.clock.tick(60)

Game().run()
