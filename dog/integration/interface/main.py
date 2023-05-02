import sys
import ctypes

if __name__ == '__main__':
    libfile = r"integration\interface\src\clib.so"
    lib = ctypes.cdll.LoadLibrary(libfile)

    x = 6

    answer = lib.clib(x)
    print(answer)