from gridData import Grid
import numpy as np
import sys

sys.path.append("/home/abdullah/Code/Python/SFED/")
from gridcollector import GridCollector
from SFED_routines import sfed_kh_3drism, integrate_sfed

gc3methbut1e = GridCollector("3methbut1e", "/home/abdullah/Code/Python/SFED/data/DATA/KH/3methbut1e/3")
gc3methbut1ol = GridCollector("3methbut1ol", "/home/abdullah/Code/Python/SFED/data/DATA/KH/3methbut1ol/3")
gc24dimepen = GridCollector("24dimepen", "/home/abdullah/Code/Python/SFED/data/DATA/KH/24dimepen/3")
gcethene = GridCollector("ethene", "/home/abdullah/Code/Python/SFED/data/DATA/KH/ethene/3")
gcethylbenzene = GridCollector("ethylbenzene", "/home/abdullah/Code/Python/SFED/data/DATA/KH/ethylbenzene/3")
gcn_decane = GridCollector("n_decane", "/home/abdullah/Code/Python/SFED/data/DATA/KH/n_decane/3")
gcn_hexane = GridCollector("n_hexane", "/home/abdullah/Code/Python/SFED/data/DATA/KH/n_hexane/3")
gcphenol = GridCollector("phenol", "/home/abdullah/Code/Python/SFED/data/DATA/KH/phenol/3")

prec = 4


def test_3methbut1e():
    sfed_o = sfed_kh_3drism(gc3methbut1e.grids["HO"].grid, gc3methbut1e.grids["CO"].grid, gc3methbut1e.grids["HH1"].grid, gc3methbut1e.grids["CH1"].grid)
    sfe = integrate_sfed(sfed_o, gc3methbut1e.delta)
    np.testing.assert_almost_equal(sfe, 24.038633400000002, prec)

def test_3methbut1ol():
    sfed_o = sfed_kh_3drism(gc3methbut1ol.grids["HO"].grid, gc3methbut1ol.grids["CO"].grid, gc3methbut1ol.grids["HH1"].grid, gc3methbut1ol.grids["CH1"].grid)
    sfe = integrate_sfed(sfed_o, gc3methbut1ol.delta)
    np.testing.assert_almost_equal(sfe, 20.825608500000001, prec)

def test_24dimepen():
    sfed_o = sfed_kh_3drism(gc24dimepen.grids["HO"].grid, gc24dimepen.grids["CO"].grid, gc24dimepen.grids["HH1"].grid, gc24dimepen.grids["CH1"].grid)
    sfe = integrate_sfed(sfed_o, gc24dimepen.delta)
    np.testing.assert_almost_equal(sfe, 32.7440566, prec)

def test_ethene():
    sfed_o = sfed_kh_3drism(gcethene.grids["HO"].grid, gcethene.grids["CO"].grid, gcethene.grids["HH1"].grid, gcethene.grids["CH1"].grid)
    sfe = integrate_sfed(sfed_o, gcethene.delta)
    np.testing.assert_almost_equal(sfe, 11.829603599999999, prec)

def test_ethylbenzene():
    sfed_o = sfed_kh_3drism(gcethylbenzene.grids["HO"].grid, gcethylbenzene.grids["CO"].grid, gcethylbenzene.grids["HH1"].grid, gcethylbenzene.grids["CH1"].grid)
    sfe = integrate_sfed(sfed_o, gcethylbenzene.delta)
    np.testing.assert_almost_equal(sfe, 26.079809900000001, prec)

def test_n_decane():
    sfed_o = sfed_kh_3drism(gcn_decane.grids["HO"].grid, gcn_decane.grids["CO"].grid, gcn_decane.grids["HH1"].grid, gcn_decane.grids["CH1"].grid)
    sfe = integrate_sfed(sfed_o, gcn_decane.delta)
    np.testing.assert_almost_equal(sfe, 46.888158400000009, prec)
