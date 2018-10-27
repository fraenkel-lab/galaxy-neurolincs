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

# TODO this script now needs to take into account level1_fastq / level2_bam / level3_vcf

if __name__ == '__main__':

    base_path = Path('/pool/data/globus/PUSHED_FROM_NYGC')
    files = [f for f in base_path.glob('**/*.*') if f.is_file()]

    for filepath in files:

        if filepath.suffix == '.md5': os.remove(filepath)

        else:
            filepath_parts = filepath.split('/')

            CGND_ID = [part for part in filepath_parts if 'CGND_' in part and len(part) == 10]
            assert len(CGND_ID) == 1

            sample_name = [part for part in filepath_parts if 'Sample_' in part]
            assert len(sample_name) == 0 or len(sample_name) == 1

            file_string = filepath_parts[-1]

            if len(sample_name) == 0:

                if 'StructuralVariants' in filepath:
                    os.renames(filepath, base_path / '3_vcf' / CGND_ID / 'StructuralVariants' / file_string)
                elif 'ExpansionHunter' in filepath:
                    os.renames(filepath, base_path / '3_vcf' / CGND_ID / 'ExpansionHunter' / file_string)
                else: print('no sample name in: ' + filepath)

            elif len(sample_name) == 1:

                data_level = 0
                if '.fastq.gz' in file_string:
                    data_level = '1_fastq'

                if '.bam' in file_string or'.bai' in file_string or'.cram' in file_string or'.crai' in file_string:
                    data_level = '2_bam'

                if ('.haplotypeCalls.er.raw.vcf.gz' in file_string or
                    '.haplotypeCalls.er.raw.vcf.gz.tbi' in file_string or
                    '.recalibrated.haplotypeCalls.vcf.gz' in file_string or
                    '.recalibrated.haplotypeCalls.vcf.gz.tbi' in file_string or
                    '.recalibrated.haplotypeCalls.annotated.vcf.gz' in file_string or
                    '.recalibrated.haplotypeCalls.annotated.vcf.gz.tbi' in file_string or
                    '.recalibrated.haplotypeCalls.annotated.clinical.txt' in file_string or
                    '.recalibrated.haplotypeCalls.annotated.coding.txt' in file_string or
                    '.recalibrated.haplotypeCalls.annotated.coding_rare.txt' in file_string or
                    '.recalibrated.haplotypeCalls.annotated.txt' in file_string or
                    '.genomestrip.del.bed' in file_string or
                    '.eh.vcf' in file_string):
                    data_level = '3_vcf'

                assert data_level != 0

                if 'StructuralVariants' in filepath:
                    os.renames(filepath, base_path / data_level / CGND_ID / sample_name[0] / 'StructuralVariants' / file_string)
                else:
                    os.renames(filepath, base_path / data_level / CGND_ID / sample_name[0] / file_string)

            else: print('possibly too many sample names in: ' + filepath)


    removeEmptyFolders(base_filepath)




