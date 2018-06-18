import os, sys, pickle
from pathlib import Path


def flatten(list_of_lists): return [item for sublist in list_of_lists for item in sublist]

# usage: python ~/galaxy-neurolincs/scripts/strip.py -b38 /pool/data/globus/PUSHED_FROM_NYGC

if __name__ == '__main__':

	s = sys.argv[1]
	root_dir = sys.argv[2]

	filepaths = flatten([[os.path.join(path, file) for file in files] for path, subdirs, files in os.walk(root_dir) if len(files)])

	for filepath in filepaths:
		os.renames(filepath, filepath.replace(s,""))
