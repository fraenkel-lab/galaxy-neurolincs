import os, sys, pickle
from pathlib import Path


def flatten(list_of_lists): return [item for sublist in list_of_lists for item in sublist]

def removeEmptyFolders(path, removeRoot=True):

    if not os.path.isdir(path):
        return

    # remove empty subfolders
    files = os.listdir(path)
    if len(files):
        for f in files:
            fullpath = os.path.join(path, f)
            if os.path.isdir(fullpath):
                removeEmptyFolders(fullpath)

    # if folder empty, delete it
    files = os.listdir(path)
    if len(files) == 0 and removeRoot:
        os.rmdir(path)


# Usage: python3 ~/galaxy-neurolincs/scripts/clean_CGND.py

# Note: should be idempotent

if __name__ == '__main__':

    base_path = Path('/pool/data/globus/PUSHED_FROM_NYGC')
    files = [f for f in base_path.glob('**/*.*') if f.is_file()]

    for filepath in files:

        if filepath.suffix == '.md5': os.remove(filepath)

        else:

            CGND_ID = [part for part in filepath.parts if 'CGND_' in part and len(part) == 10]
            assert len(CGND_ID) == 1
            CGND_ID = CGND_ID[0]

            sample_name = [part for part in filepath.parts if 'Sample_' in part]
            assert len(sample_name) == 0 or len(sample_name) == 1

            if len(sample_name) == 0:

                if any(['StructuralVariants' in part for part in filepath.parts]):
                    os.makedirs(base_path / '3_vcf' / CGND_ID / 'StructuralVariants', exist_ok=True)
                    filepath.rename(base_path / '3_vcf' / CGND_ID / 'StructuralVariants' / filepath.name)
                elif any(['ExpansionHunter' in part for part in filepath.parts]):
                    os.makedirs(base_path / '3_vcf' / CGND_ID / 'ExpansionHunter', exist_ok=True)
                    filepath.rename(base_path / '3_vcf' / CGND_ID / 'ExpansionHunter' / filepath.name)
                else: print('no sample name in: ' + filepath)

            elif len(sample_name) == 1:

                data_level = 0
                if '.fastq.gz' in filepath.name:
                    data_level = '1_fastq'

                if '.bam' in filepath.name or'.bai' in filepath.name or'.cram' in filepath.name or'.crai' in filepath.name:
                    data_level = '2_bam'

                if ('.haplotypeCalls.er.raw.vcf.gz' in filepath.name or
                    '.haplotypeCalls.er.raw.vcf.gz.tbi' in filepath.name or
                    '.recalibrated.haplotypeCalls.vcf.gz' in filepath.name or
                    '.recalibrated.haplotypeCalls.vcf.gz.tbi' in filepath.name or
                    '.recalibrated.haplotypeCalls.annotated.vcf.gz' in filepath.name or
                    '.recalibrated.haplotypeCalls.annotated.vcf.gz.tbi' in filepath.name or
                    '.recalibrated.haplotypeCalls.annotated.clinical.txt' in filepath.name or
                    '.recalibrated.haplotypeCalls.annotated.coding.txt' in filepath.name or
                    '.recalibrated.haplotypeCalls.annotated.coding_rare.txt' in filepath.name or
                    '.recalibrated.haplotypeCalls.annotated.txt' in filepath.name or
                    '.genomestrip.del.bed' in filepath.name or
                    '.eh.vcf' in filepath.name):
                    data_level = '3_vcf'

                assert data_level != 0

                if any(['StructuralVariants' in part for part in filepath.parts]):
                    os.makedirs(base_path / data_level / CGND_ID / sample_name[0] / 'StructuralVariants', exist_ok=True)
                    filepath.rename(base_path / data_level / CGND_ID / sample_name[0] / 'StructuralVariants' / filepath.name)
                else:
                    os.makedirs(base_path / data_level / CGND_ID / sample_name[0], exist_ok=True)
                    filepath.rename(base_path / data_level / CGND_ID / sample_name[0] / filepath.name)

            else: print('possibly too many sample names in: ' + filepath)


    removeEmptyFolders(base_path)




