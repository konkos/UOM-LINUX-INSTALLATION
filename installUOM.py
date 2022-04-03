import os
from LinuxDistrosEnum import LinuxDistro


def create_package_manager_list_files():
    os.system("which apt > apt.txt")
    os.system("which dnf > dnf.txt")


def remove_package_manager_list_files():
    os.system("rm apt.txt")
    os.system("rm dnf.txt")


SYSTEM_TYPE = LinuxDistro.NOT_FOUND

if __name__ == "__main__":

    create_package_manager_list_files()

    with open("apt.txt", "r") as f:
        lines = f.readlines()
        if len(lines) > 0:
            # os.system("bash ./installUOM_DEBIAN.sh")
            SYSTEM_TYPE = LinuxDistro.APT

    with open("dnf.txt", "r") as f:
        lines = f.readlines()
        if len(lines) > 0:
            # os.system("bash ./installUOM_DNF.sh")
            SYSTEM_TYPE = LinuxDistro.DNF

    print(SYSTEM_TYPE.value)
    # remove_package_manager_list_files()
