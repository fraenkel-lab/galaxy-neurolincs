import os, sys, pickle, hashlib


if __name__ == '__main__':

	base_filepath = "/pool/data/globus/PUSHED_FROM_NYGC/nas/CGND_11418/Project_CGND_11418_B02_GRM_WGS.gVCF.2018-02-09/Sample_CGND-HDA-00001-b38/analysis"

	# for each directory,
	for directory, subdirectories, files in os.walk(base_filepath):

		# if it contains a subdirectory called checksum
		if 'checksum' in subdirectories:

			# for each file in the directory
			for file in files:

				# take the checksum
				with open(os.path.join(base_filepath, file), 'rb') as f:
					our_checksum = hashlib.md5(f.read()).hexdigest()

				# read the checksum file in checksum/
				with open(os.path.join(base_filepath, 'checksum', file+'.md5'), 'rb') as checksum_file:
					their_checksum = checksum_file.read().split()[0]

				if our_checksum != their_checksum:
					print(file)

				# compare
				# print if they're not identical.

