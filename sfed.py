from gridData import Grid, OpenDX
from SFED_routines import *
import numpy as np
import sys
import argparse
import textwrap
from gridcollector import GridCollector

parser = argparse.ArgumentParser(epilog=textwrap.dedent('''\
    The .dx files in your input directory need to be tagged with H, C and G 
    for the total correlation function, direct correlation function and 
    pair distribution function respectively.'''))

parser.add_argument("-d", "--directory", help=" Directory to be scanned containing dx files", required=True)
parser.add_argument("-i", "--input", help="Name of input molecule", required=True)
parser.add_argument("-c", "--closure", help="Closure for SFE functional [KH, HNC or GF]", required=True)
parser.add_argument("-o", "--output", help = "Output file name", required=True)
parser.add_argument("-T", "--temperature",  help="Temperature of system (default = 300)", type=float, nargs="?", default=300)
parser.add_argument("-p", "--density", help="Density of system (default = 0.03342285869 [for water])", type=float, nargs="?", default=3.3422858685000001E-02)
#parser.add_argument("-t", "--tags", help="Suffix tags for scanning the correct .dx files (default = [\"H\", \"C\", \"G\"])", nargs="+", default=["H", "C", "G"])
args = parser.parse_args()

def epilogue(output_sfed, sample_grid, fname):
    print("SFE (integrated SFED):\n", integrate_sfed(output_sfed, np.prod(sample_grid.delta)))
    writedx(output_sfed, sample_grid, fname)
    print("SFED written to " + fname + ".dx")

if __name__ == "__main__":
    data_path = args.directory
    mol_name = args.input
    #suffixes = args.tags
    grids = GridCollector(mol_name, data_path)

    if args.closure == "KH":
        output_sfed = sfed_kh_3drism(grids.grids["HO"].grid, grids.grids["CO"].grid, grids.grids["HH1"].grid, grids.grids["CH1"].grid, rho=args.density, T=args.temperature)
        epilogue(output_sfed, grids.grids["HO"], args.output)
    elif args.closure == "GF":
        output_sfed = sfed_gf_3drism(grids.grids["HO"].grid, grids.grids["CO"].grid, grids.grids["HH1"].grid, grids.grids["CH1"].grid, rho=args.density, T=args.temperature)
        epilogue(output_sfed, grids.grids["HO"].grid, args.output)
    elif args.closure == "HNC":
        output_sfed = sfed_hnc_3drism(grids.grids["HO"].grid, grids.grids["CO"].grid, grids.grids["HH1"].grid, grids.grids["CH1"].grid, rho=args.density, T=args.temperature)
        epilogue(output_sfed, grids.grids["HO"].grid, args.output)
    else:
        raise Exception("Unknown closure")