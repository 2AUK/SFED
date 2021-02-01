from gridData import Grid, OpenDX
from SFED_routines import *
import numpy as np
import sys
import argparse
from gridcollector import GridCollector

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--directory", help=" Directory to be scanned containing dx files", required=True)
parser.add_argument("-i", "--input", help="Name of input molecule", required=True)
parser.add_argument("-c", "--closure", help="Closure for SFE functional [KH, HNC or GF]", required=True)
parser.add_argument("-o", "--output", help = "Output file name", required=True)
parser.add_argument("-T", "--temperature",  help="Temperature of system (default = 300)", type=float, nargs="?", default=300)
parser.add_argument("-p", "--density", help="Density of system (default = 0.03342285869 [for water])", type=float, nargs="?", default=3.3422858685000001E-02)
""" parser.add_argument("--ho", help="[INPUT] O Total Correlation Function .dx")
parser.add_argument("--co", help="[INPUT] O Direct Correlation Function .dx")
parser.add_argument("--hh", help="[INPUT] H Total Correlation Function .dx")
parser.add_argument("--ch", help="[INPUT] H Direct Correlation Function .dx")
parser.add_argument("--uo", help="[PSEN INPUT] O Potential Energy Grid .dx")
parser.add_argument("--uh", help="[PSEN INPUT] H Potential Energy Grid .dx")
#parser.add_argument("use_gr", help="[OPTION] User g(r) function to compute h(r)[= g(r) - 1], 1 (yes) or 0 (no)", action="store_true")
#parser.add_argument("go", help="[INPUT, OPTIONAL] O RDF .dx")
#parser.add_argument("gh", help="[INPUT, OPTIONAL] H RDF .dx")
parser.add_argument("-c", "--closure", help="closure for SFE functional [KH, HNC or GF]")
parser.add_argument("-o", "--output", help = "Output file name")
parser.add_argument("--temperature", help="Temperature of system (default = 300)", type=float, nargs="?", default=300)
parser.add_argument("--rho", help="Density of system (default = 0.03342285869 [for water])", type=float, nargs="?", default=0.03342285869) """
args = parser.parse_args()

def epilogue(output_sfed, sample_grid, fname):
    print("SFE (integrated SFED):\n", integrate_sfed(output_sfed, np.prod(sample_grid.delta)))
    writedx(output_sfed, sample_grid, fname)
    print("SFED written to " + fname + ".dx")

if __name__ == "__main__":
    data_path = args.directory
    mol_name = args.input
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

