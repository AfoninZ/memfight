import pygame
import virtual.machine as vm
from virtual.cell import CellFlags


pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

m = vm.VirtualMachine()
m.mem_populate()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # m.mem_damage(0.00001)
    for y in range(25):
        for x in range(60):
            cell = m.mem_getidx(y * 60 + x)
            if cell.get_flag() == CellFlags.EMPTY:
                pygame.draw.rect(screen, (127, 127, 127), ((2 + (x * 12), 2 + (y * 12)), (10, 10)), 0)
            elif cell.get_flag() == CellFlags.DAMAGED:
                pygame.draw.rect(screen, (64, 64, 64), ((2 + (x * 12), 2 + (y * 12)), (10, 10)), 0)
            else:
                color = cell.get_color()
                rgb = (170, 170, 170)
                if color == 1:
                    rgb = (170, 0, 0)
                elif color == 2:
                    rgb = (0, 0, 170)
                elif color == 3:
                    rgb = (0, 170, 0)
                if cell.get_flag() == CellFlags.MODIFIED:
                    rgb = tuple(map(lambda a: min(255, a * 2), rgb))
                pygame.draw.rect(screen, rgb, ((2 + (x * 12), 2 + (y * 12)), (10, 10)), 0)
    pygame.display.flip()

pygame.quit()
