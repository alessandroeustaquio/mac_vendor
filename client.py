from os import linesep
import requests

def ler_txt():
    macs = {}
    with open('MACs.txt', 'r') as fp:
        lines = fp.readlines()
        #macs = [line.rstrip() for line in lines]
        # mesma coisa que acima
        if lines:
            for line in lines:
                line = line.rstrip()
                line_array = line.split(";")
                ip=line_array[0]
                mac=line_array[1]
                macs[ip]=mac
    print(line_array)
    return macs
print(m)
