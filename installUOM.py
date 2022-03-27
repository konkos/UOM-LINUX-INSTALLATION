import platform

if __name__=="__main__":

    u_name = platform.uname()

    linux_distro = u_name[3]

    for item in linux_distro.split():
        print(item)
