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

# python3 ~/galaxy-neurolincs/scripts/sync_nygc_push.py

# TODO: make sure the time comparison is correct, someday...

if __name__ == '__main__':

    srcdir = Path('/pool/data/globus/PUSHED_FROM_NYGC')
    targetdir = Path('/pool/data/globus/other_genomics')

    new_files = [f.relative_to(srcdir) for f in srcdir.glob('**/*.*') if f.is_file()]
    old_files = [f.relative_to(targetdir) for f in targetdir.glob('**/*.*') if f.is_file()]

    # Handle new files
    all_new_files = list(set(new_files) - set(old_files))

    for file in all_new_files:

        os.makedirs((targetdir / file.parent), exist_ok=True)
        (srcdir / file).rename(targetdir / file)

    # Handle updated files
    all_updated_files = list(set(all_pushed_files) & set(all_local_files))

    for file in all_updated_files:

        if (srcdir / file).stat().st_mtime > (targetdir / file).stat().st_mtime:

            os.makedirs((targetdir / file.parent), exist_ok=True)
            (srcdir / file).rename(targetdir / file)

        else:

            print("Files which we seem to have more recent copies of in "+srcdir+":")
            print(file)

    removeEmptyFolders(srcdir)
