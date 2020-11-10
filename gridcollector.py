from gridData import Grid
import numpy as np
import re
from pathlib import Path
from SFED_routines import sfed_kh_3drism, integrate_sfed

class GridCollector():

    def __init__(self, mol, fname, suffix=["H", "C", "G", "U"]):
        self.mol = mol
        self.fname = fname
        self.suffix = suffix
        self.delta = None
        self.grids = {}
        self.__U_loaded = False
        self.read()

    def read(self):
        DX = Path(self.fname).glob("*.dx")
        files = [p for p in DX if p.is_file()]
        for dx in files:
            name = dx.stem.split('.')
            if (name[0].endswith("_"+self.suffix[0])):
                self.grids[self.suffix[0]+name[1]] = Grid(self.fname + "/" + dx.stem + ".dx")
                self.delta = np.prod(self.grids[self.suffix[0]+name[1]].delta)
            elif (name[0].endswith("_"+self.suffix[1])):
                self.grids[self.suffix[1]+name[1]] = Grid(self.fname + "/" + dx.stem + ".dx")
            elif (name[0].endswith("_"+self.suffix[2])):
                self.grids[self.suffix[2]+name[1]] = Grid(self.fname + "/" + dx.stem + ".dx")
            elif (name[0].endswith("_"+self.suffix[3])):
                self.grids[self.suffix[3]+name[1]] = Grid(self.fname + "/" + dx.stem + ".dx")