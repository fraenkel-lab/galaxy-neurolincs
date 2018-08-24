import os
import collections

base_path = "/pool/data/globus"


def link(source, dest):

    os.makedirs((base_path+dest).rsplit('/', 1)[0], exist_ok=True)

    try:
        os.link(base_path+source, base_path+dest)
    except FileExistsError:
        print("found an existing file at "+dest)
        print("... updating hard link to "+source, end="\n\n")
        os.remove(base_path+dest)
        os.link(base_path+source, base_path+dest)


def links(list_of_sources_and_dests):

    counts = collections.Counter([dest for source,dest in list_of_sources_and_dests])

    for source, dest in list_of_sources_and_dests:
        if counts[dest] == 1: link(source, dest)

    duplicated = [dest for dest, count in counts.items() if count > 1]

    for dup_dest in duplicated:
        os.makedirs((base_path+dup_dest).rsplit('/', 1)[0], exist_ok=True)

        sources = [source for source, dest in list_of_sources_and_dests if dest == dup_dest]

        print("duplicated destination "+dup_dest+" concatenating files...")

        with open(base_path+dup_dest, 'w') as outfile:
            for source in sources:
                print("    "+source)
                with open(base_path+source) as infile:
                    for line in infile:
                        outfile.write(line)


