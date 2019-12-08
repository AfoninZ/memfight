from virtual.cell import Cell, CellFlags
from random import random, randint


class VirtualMachine:
    def __init__(self):
        self.mem = [Cell(CellFlags.EMPTY, 0, 0x00) for i in range(1500)]

    def mem_damage(self, prob):
        for cell in self.mem:
            if random() < prob:
                cell.set_flag(CellFlags.DAMAGED)
                cell.set_value(randint(0, 255))

    def mem_getidx(self, idx):
        return self.mem[idx]