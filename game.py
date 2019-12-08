import pygame
import virtual.machine as vm
from virtual.cell import CellFlags


pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

m = vm.VirtualMachine()

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
    pygame.display.flip()

pygame.quit()
