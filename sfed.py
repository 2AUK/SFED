from gridData import Grid, OpenDX
from SFED_routines import *
import numpy as np
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--ho", help="[INPUT] O Total Correlation Function .dx")
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
parser.add_argument("--temp", help="Temperature of system (default = 300)", type=float, nargs="?", default=300)
parser.add_argument("--rho", help="Density of system (default = 0.03342285869 [for water])", type=float, nargs="?", default=0.03342285869)
args = parser.parse_args()

def epilogue(output_sfed, sample_grid, fname):
    print("SFE (integrated SFED):\n", integrate_sfed(output_sfed, np.prod(sample_grid.delta)))
    writedx(output_sfed, sample_grid, fname)
    print("SFED written to " + fname + ".dx")

if __name__ == "__main__":
    ho = Grid(args.ho)
    co = Grid(args.co)
    hh = Grid(args.hh)
    ch = Grid(args.ch)

    if args.closure == "KH":
        output_sfed = sfed_kh_3drism(ho.grid, co.grid, hh.grid, ch.grid, rho=args.rho, T=args.temp)
        epilogue(output_sfed, ho, args.output)
    elif args.closure == "GF":
        output_sfed = sfed_gf_3drism(ho.grid, co.grid, hh.grid, ch.grid, rho=args.rho, T=args.temp)
        epilogue(output_sfed, ho, args.output)
    elif args.closure == "HNC":
        output_sfed = sfed_hnc_3drism(ho.grid, co.grid, hh.grid, ch.grid, rho=args.rho, T=args.temp)
        epilogue(output_sfed, ho, args.output)
    else:
        print("Closure not implemented.")

