from gridData import Grid
import numpy as np
import sys

sys.path.append("/home/abdullah/Code/Python/SFED/")
from gridcollector import GridCollector
from SFED_routines import sfed_psen_3drism, sfed_hnc_3drism, integrate_sfed
from pathlib import Path

base_path = Path(__file__).parent
data_path = file_path = (base_path / "../data/DATA/PSE3/").resolve()

gc3methbut1e = GridCollector("3methbut1e", str(data_path) + "/3methbut1e/3")
gc3methbut1ol = GridCollector("3methbut1ol", str(data_path) + "/3methbut1ol/3")
gc24dimepen = GridCollector("24dimepen", str(data_path) + "/24dimepen/3")
gcethene = GridCollector("ethene", str(data_path) + "/ethene/3")
gcethylbenzene = GridCollector("ethylbenzene", str(data_path) + "/ethylbenzene/3")
gcn_decane = GridCollector("n_decane", str(data_path) + "/n_decane/3")
gcn_hexane = GridCollector("n_hexane", str(data_path) + "/n_hexane/3")
gcphenol = GridCollector("phenol", str(data_path) + "/phenol/3")

prec = 4


# def test_3methbut1e():
#     sfed_o = sfed_psen_3drism(gc3methbut1e.grids["HO"].grid, gc3methbut1e.grids["CO"].grid, gc3methbut1e.grids["HH1"].grid, gc3methbut1e.grids["CH1"].grid, gc3methbut1e.grids["UO"].grid, gc3methbut1e.grids["UH1"].grid, 3.0, rho=0.03342285869, kB=0.00198721587, T=300, Na=6.022142E23)
#     sfe_pse = integrate_sfed(sfed_o, gc3methbut1e.delta)
#     sfed_hnc = sfed_hnc_3drism(gc3methbut1e.grids["HO"].grid, gc3methbut1e.grids["CO"].grid, gc3methbut1e.grids["HH1"].grid, gc3methbut1e.grids["CH1"].grid)
#     sfe_hnc = integrate_sfed(sfed_hnc, gc3methbut1e.delta)
#     np.testing.assert_almost_equal(sfe_hnc - sfe_pse, 20.2375, prec)

# def test_3methbut1ol():
#     sfed_o = sfed_kh_3drism(gc3methbut1ol.grids["HO"].grid, gc3methbut1ol.grids["CO"].grid, gc3methbut1ol.grids["HH1"].grid, gc3methbut1ol.grids["CH1"].grid)
#     sfe = integrate_sfed(sfed_o, gc3methbut1ol.delta)
#     np.testing.assert_almost_equal(sfe, 20.825608500000001, prec)

# def test_24dimepen():
#     sfed_o = sfed_kh_3drism(gc24dimepen.grids["HO"].grid, gc24dimepen.grids["CO"].grid, gc24dimepen.grids["HH1"].grid, gc24dimepen.grids["CH1"].grid)
#     sfe = integrate_sfed(sfed_o, gc24dimepen.delta)
#     np.testing.assert_almost_equal(sfe, 32.7440566, prec)

# def test_ethene():
#     sfed_o = sfed_kh_3drism(gcethene.grids["HO"].grid, gcethene.grids["CO"].grid, gcethene.grids["HH1"].grid, gcethene.grids["CH1"].grid)
#     sfe = integrate_sfed(sfed_o, gcethene.delta)
#     np.testing.assert_almost_equal(sfe, 11.829603599999999, prec)

# def test_ethylbenzene():
#     sfed_o = sfed_kh_3drism(gcethylbenzene.grids["HO"].grid, gcethylbenzene.grids["CO"].grid, gcethylbenzene.grids["HH1"].grid, gcethylbenzene.grids["CH1"].grid)
#     sfe = integrate_sfed(sfed_o, gcethylbenzene.delta)
#     np.testing.assert_almost_equal(sfe, 26.079809900000001, prec)

# def test_n_decane():
#     sfed_o = sfed_kh_3drism(gcn_decane.grids["HO"].grid, gcn_decane.grids["CO"].grid, gcn_decane.grids["HH1"].grid, gcn_decane.grids["CH1"].grid)
#     sfe = integrate_sfed(sfed_o, gcn_decane.delta)
#     np.testing.assert_almost_equal(sfe, 46.888158400000009, prec)

# def test_n_hexane():
#     sfed_o = sfed_kh_3drism(gcn_hexane.grids["HO"].grid, gcn_hexane.grids["CO"].grid, gcn_hexane.grids["HH1"].grid, gcn_hexane.grids["CH1"].grid)
#     sfe = integrate_sfed(sfed_o, gcn_hexane.delta)
#     np.testing.assert_almost_equal(sfe, 30.277262180000001, prec)

# def test_phenol():
#     sfed_o = sfed_kh_3drism(gcphenol.grids["HO"].grid, gcphenol.grids["CO"].grid, gcphenol.grids["HH1"].grid, gcphenol.grids["CH1"].grid)
#     sfe = integrate_sfed(sfed_o, gcphenol.delta)
#     np.testing.assert_almost_equal(sfe, 13.918498, prec)

# def test_nhexylbenzene():
#     sfed_o = sfed_kh_3drism(gcnhexylbenzene.grids["HO"].grid, gcnhexylbenzene.grids["CO"].grid, gcnhexylbenzene.grids["HH1"].grid, gcnhexylbenzene.grids["CH1"].grid)
#     sfe = integrate_sfed(sfed_o, gcnhexylbenzene.delta)
#     np.testing.assert_almost_equal(sfe, 42.573009200000008, prec)

