import os, sys, pickle

def flatten(list_of_lists): return [item for sublist in list_of_lists for item in sublist]

def all_subfiles(path): return flatten([[os.path.join(p, file) for file in files] for p, subdirs, files in os.walk(path) if len(files)])

def all_genomics_subfiles(path): return [file for file in all_subfiles(path) if "Sample_" in file]

if __name__ == '__main__':

    genomics                   = all_genomics_subfiles("/pool/data/globus/genomics/")
    # other_genomics             = all_genomics_subfiles("/pool/data/globus/genomics_other/")

    epigenomics                = all_subfiles("/pool/data/globus/epigenomics/")
    proteomics                 = all_subfiles("/pool/data/globus/proteomics/")
    transcriptomics            = all_subfiles("/pool/data/globus/transcriptomics/")


    files = genomics + neurolincs_genomics + epigenomics + proteomics + transcriptomics

    [print(file) for file in files]

