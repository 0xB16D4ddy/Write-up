#!/usr/bin/env python3
import requests 
import re
from html import unescape


with open('natas6.html','a') as out:

    username = "natas6"
    password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'
    s = requests.session()


    url = 'http://%s.natas.labs.overthewire.org' % username

    # r = s.get(url, auth = (username, password))
    # r = s.get(url + "/index-source.html", auth = (username, password))
    r = s.post(url,data = {"secret" : "submit"} , auth = (username, password))
    content =  r.text

    out.write(unescape(content))


# print(re.findall('The password for natas6 is (.*)</div>',content)[0])


'''
    #decode html
    html = """\\u003Cdiv id=\\u0022contenedor\\u0022\\u003E \\u003Ch2 class=\\u0022text-left m-b-2\\u0022\\u003EInformaci\\u00f3n del veh\\u00edculo de patente AA345AA\\u003C\\/h2\\u003E\\n\\n\\n\\n \\u003Cdiv class=\\u0022panel panel-default panel-disabled m-b-2\\u0022\\u003E\\n \\u003Cdiv class=\\u0022panel-body\\u0022\\u003E\\n \\u003Ch2 class=\\u0022table_title m-b-2\\u0022\\u003EInformaci\\u00f3n del Registro Automotor\\u003C\\/h2\\u003E\\n \\u003Cdiv class=\\u0022col-md-6\\u0022\\u003E\\n \\u003Clabel class=\\u0022control-label\\u0022\\u003ERegistro Seccional\\u003C\\/label\\u003E\\n \\u003Cp\\u003ESAN MIGUEL N\\u00b0 1\\u003C\\/p\\u003E\\n \\u003Clabel class=\\u0022control-label\\u0022\\u003EDirecci\\u00f3n\\u003C\\/label\\u003E\\n \\u003Cp\\u003EMAESTRO ANGEL D\\u0027ELIA 766\\u003C\\/p\\u003E\\n \\u003Clabel class=\\u0022control-label\\u0022\\u003EPiso\\u003C\\/label\\u003E\\n \\u003Cp\\u003EPB\\u003C\\/p\\u003E\\n \\u003Clabel class=\\u0022control-label\\u0022\\u003EDepartamento\\u003C\\/label\\u003E\\n \\u003Cp\\u003E-\\u003C\\/p\\u003E\\n \\u003Clabel class=\\u0022control-label\\u0022\\u003EC\\u00f3digo postal\\u003C\\/label\\u003E\\n \\u003Cp\\u003E1663\\u003C\\/p\\u003E\\n \\u003C\\/div\\u003E\\n \\u003Cdiv class=\\u0022col-md-6\\u0022\\u003E\\n \\u003Clabel class=\\u0022control-label\\u0022\\u003ELocalidad\\u003C\\/label\\u003E\\n \\u003Cp\\u003ESAN MIGUEL\\u003C\\/p\\u003E\\n \\u003Clabel class=\\u0022control-label\\u0022\\u003EProvincia\\u003C\\/label\\u003E\\n \\u003Cp\\u003EBUENOS AIRES\\u003C\\/p\\u003E\\n \\u003Clabel class=\\u0022control-label\\u0022\\u003ETel\\u00e9fono\\u003C\\/label\\u003E\\n \\u003Cp\\u003E(11)46646647\\u003C\\/p\\u003E\\n \\u003Clabel class=\\u0022control-label\\u0022\\u003EHorario\\u003C\\/label\\u003E\\n \\u003Cp\\u003E08:30 a 12:30\\u003C\\/p\\u003E\\n \\u003C\\/div\\u003E\\n \\u003C\\/div\\u003E\\n\\u003C\\/div\\u003E \\n\\n\\u003Cp class=\\u0022text-center m-t-3 m-b-1 hidden-print\\u0022\\u003E\\n \\u003Ca href=\\u0022javascript:window.print();\\u0022 class=\\u0022btn btn-default\\u0022\\u003EImprim\\u00ed la consulta\\u003C\\/a\\u003E \\u0026nbsp; \\u0026nbsp;\\n \\u003Ca href=\\u0022\\u0022 class=\\u0022btn use-ajax btn-primary\\u0022\\u003EHacer otra consulta\\u003C\\/a\\u003E\\n\\u003C\\/p\\u003E\\n\\u003C\\/div\\u003E"""


print(unescape(html.replace("\\/", "/").encode().decode('unicode_escape')))
#print(unescape(html))
'''