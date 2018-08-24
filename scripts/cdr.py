import os, sys, pickle

def flatten(list_of_lists): return [item for sublist in list_of_lists for item in sublist]

def all_subfiles(path): return flatten([[os.path.join(p, file) for file in files] for p, subdirs, files in os.walk(path) if len(files)])

def all_genomics_subfiles(path): return [file for file in all_subfiles(path) if "Sample_" in file]

if __name__ == '__main__':

    aals_epigenomics           = all_subfiles("/pool/data/globus/aals_epigenomics/")
    aals_genomics              = all_genomics_subfiles("/pool/data/globus/aals_genomics/")
    aals_proteomics            = all_subfiles("/pool/data/globus/aals_proteomics/")
    aals_transcriptomics       = all_subfiles("/pool/data/globus/aals_transcriptomics/")
    neurolincs_epigenomics     = all_subfiles("/pool/data/globus/neurolincs_epigenomics/")
    neurolincs_genomics        = all_genomics_subfiles("/pool/data/globus/neurolincs_genomics/")
    neurolincs_proteomics      = all_subfiles("/pool/data/globus/neurolincs_proteomics/")
    neurolincs_transcriptomics = all_subfiles("/pool/data/globus/neurolincs_transcriptomics/")
    # other_genomics             = all_genomics_subfiles("/pool/data/globus/other_genomics/")

    files = aals_epigenomics + aals_genomics + aals_proteomics + aals_transcriptomics + neurolincs_epigenomics + neurolincs_genomics + neurolincs_proteomics + neurolincs_transcriptomics #+ other_genomics

    [print(file) for file in files]

