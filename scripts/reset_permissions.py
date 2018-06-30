import os
import pwd
import grp
import shutil
from pathlib import Path


desired_users = ['root', 'sync', 'localskm', 'stacia', 'pulkit', 'greg',
                'galaxy', 'vidya', 'andrea', 'lilith', 'leandro', 'jenny',
                'barry', 'terri', 'blah', 'skm', 'lenail', 'fraenkel', 'iamjli' ]

desired_groups = {
    'mit' : ['iamjli', 'skm', 'fraenkel', 'lenail'],
    'ucsf': ['leandro'],
    'uci' : ['jenny'],
    'cshs': ['vidya','andrea','lilith'],
    'nygc': ['pulkit'],
    'pm'  : ['barry', 'terri'],
    'aals_members': ['iamjli','skm','fraenkel','lenail','leandro','jenny','vidya','andrea','lilith','barry','terri'],
}

mode = {
    'owner can do anything, group can read and execute, others have no permissions': 0o755,
    'owner can do anything, group can do anything, others have no permissions': 0o775,
}

root_filepath = Path('/pool/data/globus/')
desired_ownerships = {
    'aals_epigenomics'           : {'owner':'root', 'group':'aals_members', 'mode':mode['owner can do anything, group can read and execute, others have no permissions']},
    'aals_genomics'              : {'owner':'root', 'group':'aals_members', 'mode':mode['owner can do anything, group can read and execute, others have no permissions']},
    'aals_proteomics'            : {'owner':'root', 'group':'aals_members', 'mode':mode['owner can do anything, group can read and execute, others have no permissions']},
    'aals_transcriptomics'       : {'owner':'root', 'group':'aals_members', 'mode':mode['owner can do anything, group can read and execute, others have no permissions']},
    'neurolincs_epigenomics'     : {'owner':'root', 'group':'aals_members', 'mode':mode['owner can do anything, group can read and execute, others have no permissions']},
    'neurolincs_genomics'        : {'owner':'root', 'group':'aals_members', 'mode':mode['owner can do anything, group can read and execute, others have no permissions']},
    'neurolincs_proteomics'      : {'owner':'root', 'group':'aals_members', 'mode':mode['owner can do anything, group can read and execute, others have no permissions']},
    'neurolincs_transcriptomics' : {'owner':'root', 'group':'aals_members', 'mode':mode['owner can do anything, group can read and execute, others have no permissions']},
    'other_genomics'             : {'owner':'root', 'group':'aals_members', 'mode':mode['owner can do anything, group can read and execute, others have no permissions']},
    'PUSHED_FROM_CEDARS'         : {                'group':'cshs',         'mode':mode['owner can do anything, group can do anything, others have no permissions']},
    'PUSHED_FROM_GALAXY'         : {                'group':'galaxy',       'mode':mode['owner can do anything, group can do anything, others have no permissions']},
    'PUSHED_FROM_MIT'            : {                'group':'mit',          'mode':mode['owner can do anything, group can do anything, others have no permissions']},
    'PUSHED_FROM_NYGC'           : {                'group':'nygc',         'mode':mode['owner can do anything, group can do anything, others have no permissions']},
    'PUSHED_FROM_UCI'            : {                'group':'uci',          'mode':mode['owner can do anything, group can do anything, others have no permissions']},
    'PUSHED_FROM_UCSF'           : {                'group':'ucsf',         'mode':mode['owner can do anything, group can do anything, others have no permissions']},
    'RNAseq_base'                : {                'group':'mit',          'mode':mode['owner can do anything, group can do anything, others have no permissions']},
    'tmp'                        : {                'group':'mit',          'mode':mode['owner can do anything, group can do anything, others have no permissions']},
}



def reset_file_permissions():

    assert users_valid()
    assert groups_valid()

    for directory, permissions in desired_ownerships.items():

        new_owner = permissions.get('owner', default=None)
        new_group = permissions.get('group', default=None)
        new_mode  = permissions.get('mode', default=None)

        for dir, subdirs, files in os.walk(root_filepath / directory):

            dir = Path(dir)

            current_permissions = dir.stat()
            current_owner = pwd.getpwuid(current_permissions.st_uid).pw_name
            current_group = grp.getgrgid(current_permissions.st_gid).gr_name
            if current_owner != new_owner or current_group != new_group:
                print(f'Directory: {dir}, current owner: {current_owner}, current group: {current_group}, new owner: {new_owner}, new group: {new_group}')

            if new_owner: shutil.chown(dir, user=new_owner)
            if new_group: shutil.chown(dir, group=new_group)
            if new_mode:  dir.chmod(new_mode)

            for f in files:

                f = dir / f

                if new_owner: shutil.chown(f, user=new_owner)
                if new_group: shutil.chown(f, group=new_group)
                if new_mode:  f.chmod(new_mode)



def users_valid():

    system_users = ['/usr/sbin/nologin','/bin/nologin','/bin/false']

    existing_users = [user.pw_name for user in pwd.getpwall() if user.pw_shell not in system_users]

    # If there are existing users on the system which shouldn't be on the system
    if len(set(existing_users) - set(desired_users)) > 0:
        print("Users existing on the machine which are not accounted for in the script:")
        print(set(existing_users) - set(desired_users))
        print("please account for these users in the script, or deactivate them.")
        return False

    # If some set of users are missing from the system -- we want them but they aren't there
    if len(set(desired_users) - set(existing_users)) > 0:
        print("Users not existing on the machine which are listed in the script should be created with useradd:")
        print(set(desired_users) - set(existing_users))
        return False

    return True


def groups_valid():

    current_groups = {group.gr_name: group.gr_mem for group in grp.getgrall()}
    # Capture users' primary group affiliations, which may not be listed in the groups file.
    for user in [user for user in pwd.getpwall() if user.pw_shell not in system_users]:
        current_groups[grp.getgrgid(user.pw_gid).gr_name].append(user.pw_name)

    if len(set(desired_groups.keys()) - set(current_groups.keys())) > 0:
        print("Groups not existing on the machine which are listed in the script should be created:")
        print(set(desired_groups.keys()) - set(current_groups.keys()))
        return False

    for group_name, desired_members in desired_groups.items():

        current_members = current_groups[group_name]

        if len(set(desired_members) - set(current_members)) > 0:
            print(f"Group {group_name} is missing users specified in the script:")
            print(set(desired_members) - set(current_members))
            print("Please add these users to the group, or remove them from the group list in the script.")
            return False

        if len(set(current_members) - set(desired_members)) > 0:
            print(f"Group {group_name} contains users not specified in the script:")
            print(set(current_members) - set(desired_members))
            print("Please remove these users to the group, or add them from the group list in the script.")
            return False

    return True


if __name__ == '__main__':

    reset_file_permissions()

