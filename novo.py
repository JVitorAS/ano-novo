import pygame
import random

pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("2024")
clock = pygame.time.Clock()

font = pygame.font.SysFont('ThereBrat', 72)

particles = []
explosions = []

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if random.random() < 0.2:
        particle = {
            'pos': [random.randint(0, window_size[0]), window_size[1]],
            'color': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            'size': random.randint(2, 6),
            'speed': random.uniform(0.5, 2)
        }
        particles.append(particle)

    for particle in particles:
        particle['pos'][1] -= particle['speed']
        pygame.draw.circle(screen, particle['color'], particle['pos'], particle['size'])

        
        if particle['pos'][1] < 0:
            particles.remove(particle)
            explosion = {'pos': particle['pos'], 'radius': 1, 'max_radius': random.randint(30, 70),
                         'dx': random.uniform(-1, 1), 'dy': random.uniform(-1, 1)}
            explosions.append(explosion)

    for explosion in explosions[:]:
        pygame.draw.circle(screen, random.choice(colors), (int(explosion['pos'][0]), int(explosion['pos'][1])), explosion['radius'])
        explosion['radius'] += 2
        explosion['pos'][0] += explosion['dx'] * 2
        explosion['pos'][1] += explosion['dy'] * 2
        if explosion['radius'] > explosion['max_radius']:
            explosions.remove(explosion)

    color = random.choice(colors)
    text = font.render('Feliz Ano Novo!', True, color)
    text_rect = text.get_rect(center=(window_size[0] // 2, window_size[1] // 2))
    screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
