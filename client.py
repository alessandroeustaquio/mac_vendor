import requests
import json
from threading import Event

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
    return macs

def buscar_vendor(mac_address):
    url = 'https://api.macvendors.com/'
    url = url+mac_address
    print (url)
    response = requests.get(url)
    Event().wait(1)
    print(type(response.text))
    if response.status_code==200:
        #dic = json.loads(response.text)
        print (response.text)
        #return dic
    else:
        print('Erro')

macs_list=list(ler_txt().values())

for i in macs_list:
    dic = buscar_vendor(i)