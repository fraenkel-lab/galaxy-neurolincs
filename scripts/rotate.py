import os, sys, pickle

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


# Usage: python ~/galaxy-neurolincs/scripts/rotate.py /pool/data/globus/aals_genomics or /pool/data/globus/neurolincs_genomics

if __name__ == '__main__':

	base_filepath = sys.argv[1]

	files = flatten([[os.path.join(path, file) for file in files] for path, subdirs, files in os.walk(base_filepath) if len(files)])

	print('Not able to relocate:')

	for file in files:

	    fileparts = file.split('/')
	    if fileparts[4].split('_')[1] != 'genomics': print(file)
	    if fileparts[5].split('_')[0] != 'CGND': print(file)

	    if fileparts[6][:7] == 'Sample_':

	        if not ('.fastq.gz' in fileparts[7] or
	                 '.bam' in fileparts[7] or
	                 '.bai' in fileparts[7] or
	                 '.cram' in fileparts[7] or
	                 '.crai' in fileparts[7] or
	                 '.haplotypeCalls.er.raw.vcf.gz' in fileparts[7] or
	                 '.haplotypeCalls.er.raw.vcf.gz.tbi' in fileparts[7] or
	                 '.recalibrated.haplotypeCalls.vcf.gz' in fileparts[7] or
	                 '.recalibrated.haplotypeCalls.vcf.gz.tbi' in fileparts[7] or
	                 '.recalibrated.haplotypeCalls.annotated.vcf.gz' in fileparts[7] or
	                 '.recalibrated.haplotypeCalls.annotated.vcf.gz.tbi' in fileparts[7] or
	                 '.recalibrated.haplotypeCalls.annotated.clinical.txt' in fileparts[7] or
	                 '.recalibrated.haplotypeCalls.annotated.coding.txt' in fileparts[7] or
	                 '.recalibrated.haplotypeCalls.annotated.coding_rare.txt' in fileparts[7] or
	                 '.recalibrated.haplotypeCalls.annotated.txt' in fileparts[7] or
	                 '.genomestrip.del.bed' in fileparts[7] or
	                 '.eh.vcf' in fileparts[7]):
	            print(file)

	        else:
	        	if '.fastq.gz' in fileparts[7]:
	        		os.renames(file, '/'.join([fileparts[:5]] + ['level1_fastq'] + fileparts[5:]))
	        	elif ('.bam' in fileparts[7] or '.bai' in fileparts[7] or '.cram' in fileparts[7] or '.crai' in fileparts[7]):
	        		os.renames(file, '/'.join([fileparts[:5]] + ['level2_bam'] + fileparts[5:]))
	        	else:
	        		os.renames(file, '/'.join([fileparts[:5]] + ['level3_vcf'] + fileparts[5:]))

	    elif fileparts[6] == 'StructuralVariants':
			os.renames(file, '/'.join([fileparts[:5]] + ['level3_vcf'] + fileparts[5:]))

	    elif fileparts[6] == 'ExpansionHunter':
			os.renames(file, '/'.join([fileparts[:5]] + ['level3_vcf'] + fileparts[5:]))


	    else: print(file)





	removeEmptyFolders(base_filepath)




