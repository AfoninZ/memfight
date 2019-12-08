import pygame
import pygame.freetype

import virtual.machine as vm
from virtual.cell import CellFlags
import colors


pygame.init()
size = width, height = 800, 600

screen = pygame.display.set_mode(size)
grid = pygame.Surface((720, 300))

font = pygame.freetype.Font(pygame.freetype.match_font('consolas'), 24)
font.antialiased = True

m = vm.VirtualMachine()

running = True
c = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((24, 24, 24))

    for y in range(25):
        for x in range(60):
            cell = m.mem_getidx(y * 60 + x)
            if cell.get_flag() == CellFlags.EMPTY:
                pygame.draw.rect(grid, colors.flag_colors[0], ((
                    (x * 12), (y * 12)), (10, 10)), 0)
            elif cell.get_flag() == CellFlags.DAMAGED:
                pygame.draw.rect(grid, colors.flag_colors[1], ((
                    (x * 12), (y * 12)), (10, 10)), 0)
            else:
                color = cell.get_color()
                rgb = colors.team_colors[color]
                if cell.get_flag() == CellFlags.MODIFIED:
                    rgb = tuple(map(lambda a: min(255, a * 2), rgb))
                pygame.draw.rect(
                    grid, rgb, ((2 + (x * 12), 2 + (y * 12)), (10, 10)), 0)

    screen.blit(grid, ((800 - 720) // 2, 50))

    font.render_to(screen, (4, 404), f'Ticks: {c}', (200, 200, 200))
    font.render_to(screen, (4, 430),
                   f'Millis: {pygame.time.get_ticks()}', (200, 200, 200))
    font.render_to(
        screen, (4, 456), f'TPS: {c / pygame.time.get_ticks() * 1000}', (
            200, 200, 200))
    c += 1
    pygame.display.flip()

pygame.quit()
