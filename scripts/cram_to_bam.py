import os, sys, pickle

def flatten(list_of_lists): return [item for sublist in list_of_lists for item in sublist]


if __name__ == '__main__':

	pushed_files_path = "/pool/data/globus/PUSHED_FROM_NYGC/"

	fasta_path = ""

	all_pushed_files = flatten([[os.path.join(pushed_files_path, file) for file in files] for path, subdirs, files in os.walk(pushed_files_path) if len(files)])

	for filepath in all_pushed_files:

		if filepath[-5:] == '.cram':

			# os.renames(pushed_files_path+filepath, pushed_files_path+filepath)

			os.exec("samtools view -T "+fasta_path+" -b -o "+filepath[:-5]+".bam"+" "+filepath)

