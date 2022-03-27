import os

def createPackageManagerListFiles():
    os.system("which apt > apt.txt")
    os.system("which dnf > dnf.txt")

def removePackageManagerListFiles():
    os.system("rm apt.txt")
    os.system("rm dnf.txt")


if __name__=="__main__":

    createPackageManagerListFiles()
        
    with open("apt.txt", "r") as f:
        lines = f.readlines()
        if len(lines) > 0:
            os.system("bash ./installUOM_DEBIAN.sh")

    with open("dnf.txt", "r") as f:
        lines = f.readlines()
        if len(lines) > 0:
            os.system("bash ./installUOM_RPM.sh")

    removePackageManagerListFiles()