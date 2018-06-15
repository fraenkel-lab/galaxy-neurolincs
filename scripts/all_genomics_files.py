import os, sys, pickle

def flatten(list_of_lists): return [item for sublist in list_of_lists for item in sublist]

if __name__ == '__main__':

    aals_genomics = "/pool/data/globus/aals_genomics/"
    neurolincs_genomics = "/pool/data/globus/neurolincs_genomics/"
    other_genomics = "/pool/data/globus/other_genomics/"

    all_aals_files =        flatten([[os.path.join(path, file) for file in files] for path, subdirs, files in os.walk(aals_genomics) if len(files)])
    all_neurolincs_files =  flatten([[os.path.join(path, file) for file in files] for path, subdirs, files in os.walk(neurolincs_genomics) if len(files)])
    all_other_files =       flatten([[os.path.join(path, file) for file in files] for path, subdirs, files in os.walk(other_genomics) if len(files)])

    [print(file) for file in all_aals_files + all_neurolincs_files + all_other_files]

