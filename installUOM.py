import os

if __name__=="__main__":

    uname = os.popen("uname -a").read()
    print(uname)

    os_release = os.popen("cat /etc/os-release").read()
    print(os_release)

    for line in os_release.split("\n"):
        if line.startswith("ID="):
            print(line)
