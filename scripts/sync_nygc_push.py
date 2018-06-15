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


if __name__ == '__main__':

	srcdir = sys.argv[1]
	targetdir = sys.argv[2]

	pushed_files_base_filepath = "/pool/data/globus/"+srcdir
	local_files_base_filepath = "/pool/data/globus/"+targetdir

	all_pushed_files = flatten([[os.path.join(path.split(pushed_files_base_filepath)[1], file) for file in files] for path, subdirs, files in os.walk(pushed_files_base_filepath) if len(files)])
	all_local_files = flatten([[os.path.join(path.split(local_files_base_filepath)[1], file) for file in files] for path, subdirs, files in os.walk(local_files_base_filepath) if len(files)])

	# Handle new files
	all_new_files = list(set(all_pushed_files) - set(all_local_files))

	for file in all_new_files:
		os.renames(pushed_files_base_filepath+file, local_files_base_filepath+file)

	# Handle updated files
	all_updated_files = list(set(all_pushed_files) & set(all_local_files))

	print("Files which we seem to have more recent copies of: ")

	for file in all_updated_files:

		if os.path.getctime(pushed_files_base_filepath+file) > os.path.getmtime(local_files_base_filepath+file):

			os.renames(pushed_files_base_filepath+file, local_files_base_filepath+file)

		else:

			print(local_files_base_filepath+file)

	removeEmptyFolders(pushed_files_base_filepath)
