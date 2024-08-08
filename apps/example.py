"""
Example Application
===================

This file provides an example application demonstrating the usage of the multiple modules
from the lps_libraries.
"""

import os
import argparse

import lps_sp.acoustical.broadband as lps_bb
import lps_synthesis.background as lps_bg

from lps_utils.log import debug, info

def main():
    """
    Main function to demonstrate the usage of the multiple modules.
    """
    for color in lps_bb.ColoredNoises:
        debug(color)

    for rain in lps_bg.Rain:
        info(rain)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=f'{os.path.basename(__file__)} application')
    args = parser.parse_args()
    main()
