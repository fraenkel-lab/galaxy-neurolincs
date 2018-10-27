import os, sys, pickle, hashlib


if __name__ == '__main__':

	base_filepath = "/pool/data/globus/PUSHED_FROM_NYGC/"

	# for each directory,
	for directory, subdirectories, files in os.walk(base_filepath):

		# if it contains a subdirectory called checksum
		if 'checksum' in subdirectories:

			# for each file in the directory
			for file in files:

				# take the checksum
				with open(os.path.join(base_filepath, directory, file), 'rb') as f:
					our_checksum = hashlib.md5(f.read()).hexdigest()

				# read the checksum file in checksum/
				with open(os.path.join(base_filepath, directory, 'checksum', file+'.md5'), 'r') as checksum_file:
					their_checksum = checksum_file.read().split()[0]

				if str(our_checksum) != str(their_checksum):
					print()
					print(directory)
					print(file)
					print("our checksum: " + str(our_checksum))
					print("their checksum: " + str(their_checksum))
					print()

