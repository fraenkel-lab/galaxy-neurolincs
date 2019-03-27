import os, sys, pickle

def flatten(list_of_lists): return [item for sublist in list_of_lists for item in sublist]

def all_subfiles(path): return flatten([[os.path.join(p, file)+'\t'+sizeof_fmt(os.stat(os.path.join(p, file)).st_size) for file in files] for p, subdirs, files in os.walk(path) if len(files)])

def all_genomics_subfiles(path): return [file for file in all_subfiles(path) if "Sample_" in file]

def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


if __name__ == '__main__':

    genomics                   = all_genomics_subfiles("/pool/data/globus/genomics/")
    # other_genomics             = all_genomics_subfiles("/pool/data/globus/genomics_other/")

    epigenomics                = all_subfiles("/pool/data/globus/epigenomics/")
    proteomics                 = all_subfiles("/pool/data/globus/proteomics/")
    transcriptomics            = all_subfiles("/pool/data/globus/transcriptomics/")


    files = genomics + epigenomics + proteomics + transcriptomics

    [print(file) for file in files]

