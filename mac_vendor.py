import requests
import json
import time

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
    url = 'https://api.maclookup.app/v2/macs/'
    url = f'{url}{mac_address}'
    #print (url)
    response = requests.get(url)
    time.sleep(.2)
    #print(type(response.text))
    if response.status_code==200:
        dic = json.loads(response.text)
        return dic
    else:
        print('Erro')

macs_list=list(ler_txt().values())

for i in macs_list:
    dic = buscar_vendor(i)
    fabricante=dic.get('company')
    print (f'O fabricante do MAC: {i} é: {fabricante}')