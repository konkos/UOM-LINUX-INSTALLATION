from enum import Enum


class LinuxDistro(Enum):
    NOT_FOUND = 0
    RPM = 1
    DNF = 2
    APT = 3
