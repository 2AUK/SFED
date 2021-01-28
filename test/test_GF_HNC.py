from gridData import Grid
import numpy as np
import sys

sys.path.append("/home/abdullah/Code/Python/SFED/")
from gridcollector import GridCollector
from SFED_routines import sfed_gf_3drism, integrate_sfed
from pathlib import Path

base_path = Path(__file__).parent
data_path = file_path = (base_path / "../data/DATA/HNC/").resolve()

gc3methbut1e = GridCollector("3methbut1e", str(data_path) + "/3methbut1e/3")
gc3methbut1ol = GridCollector("3methbut1ol", str(data_path) + "/3methbut1ol/3")
gc24dimepen = GridCollector("24dimepen", str(data_path) + "/24dimepen/3")
gcethene = GridCollector("ethene", str(data_path) + "/ethene/3")
gcethylbenzene = GridCollector("ethylbenzene", str(data_path) + "/ethylbenzene/3")
gcn_decane = GridCollector("n_decane", str(data_path) + "/n_decane/3")
gcn_hexane = GridCollector("n_hexane", str(data_path) + "/n_hexane/3")
gcphenol = GridCollector("phenol", str(data_path) + "/phenol/3")
gcnhexylbenzene = GridCollector("nhexylbenzene", str(data_path )+ "/nhexylbenzene/3")

prec = 3

def test_hnc_3methbut1e():
    sfed_o = sfed_gf_3drism(gc3methbut1e.grids["HO"].grid, gc3methbut1e.grids["CO"].grid, gc3methbut1e.grids["HH1"].grid, gc3methbut1e.grids["CH1"].grid)
    sfe = integrate_sfed(sfed_o, gc3methbut1e.delta)
    np.testing.assert_almost_equal(sfe, 8.0294615000000036, prec)

def test_hnc_3methbut1ol():
    sfed_o = sfed_gf_3drism(gc3methbut1ol.grids["HO"].grid, gc3methbut1ol.grids["CO"].grid, gc3methbut1ol.grids["HH1"].grid, gc3methbut1ol.grids["CH1"].grid)
    sfe = integrate_sfed(sfed_o, gc3methbut1ol.delta)
    np.testing.assert_almost_equal(sfe, 1.4888779999999997, prec)

def test_hnc_24dimepen():
    sfed_o = sfed_gf_3drism(gc24dimepen.grids["HO"].grid, gc24dimepen.grids["CO"].grid, gc24dimepen.grids["HH1"].grid, gc24dimepen.grids["CH1"].grid)
    sfe = integrate_sfed(sfed_o, gc24dimepen.delta)
    np.testing.assert_almost_equal(sfe, 11.340047900000002, prec)

def test_hnc_ethene():
    sfed_o = sfed_gf_3drism(gcethene.grids["HO"].grid, gcethene.grids["CO"].grid, gcethene.grids["HH1"].grid, gcethene.grids["CH1"].grid)
    sfe = integrate_sfed(sfed_o, gcethene.delta)
    np.testing.assert_almost_equal(sfe, 4.5047478999999999, prec)

def test_hnc_ethylbenzene():
    sfed_o = sfed_gf_3drism(gcethylbenzene.grids["HO"].grid, gcethylbenzene.grids["CO"].grid, gcethylbenzene.grids["HH1"].grid, gcethylbenzene.grids["CH1"].grid)
    sfe = integrate_sfed(sfed_o, gcethylbenzene.delta)
    np.testing.assert_almost_equal(sfe, 4.6103786999999983, prec)

def test_hnc_n_decane():
    sfed_o = sfed_gf_3drism(gcn_decane.grids["HO"].grid, gcn_decane.grids["CO"].grid, gcn_decane.grids["HH1"].grid, gcn_decane.grids["CH1"].grid)
    sfe = integrate_sfed(sfed_o, gcn_decane.delta)
    np.testing.assert_almost_equal(sfe, 15.928665999999993, prec)

def test_hnc_n_hexane():
    sfed_o = sfed_gf_3drism(gcn_hexane.grids["HO"].grid, gcn_hexane.grids["CO"].grid, gcn_hexane.grids["HH1"].grid, gcn_hexane.grids["CH1"].grid)
    sfe = integrate_sfed(sfed_o, gcn_hexane.delta)
    np.testing.assert_almost_equal(sfe, 10.272555799999999, prec)

def test_hnc_phenol():
    sfed_o = sfed_gf_3drism(gcphenol.grids["HO"].grid, gcphenol.grids["CO"].grid, gcphenol.grids["HH1"].grid, gcphenol.grids["CH1"].grid)
    sfe = integrate_sfed(sfed_o, gcphenol.delta)
    np.testing.assert_almost_equal(sfe, -3.90118480000001, prec)

def test_hnc_nhexylbenzene():
    sfed_o = sfed_gf_3drism(gcnhexylbenzene.grids["HO"].grid, gcnhexylbenzene.grids["CO"].grid, gcnhexylbenzene.grids["HH1"].grid, gcnhexylbenzene.grids["CH1"].grid)
    sfe = integrate_sfed(sfed_o, gcnhexylbenzene.delta)
    np.testing.assert_almost_equal(sfe, 10.6374177, prec)