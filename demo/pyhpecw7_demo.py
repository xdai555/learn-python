from pyhpecw7.comware import HPCOM7
from pyhpecw7.features.interface import Interface
from pyhpecw7.features.vlan import Vlan
import logging
logging.basicConfig(level=logging.DEBUG)

host = {
    'host': '192.168.56.20',
    'username': 'netdevops',
    'password': 'netdevops',
    'port': 830,
    'device_params': {'name': 'h3c'},
}

conn = HPCOM7(**host)
conn.open()

interface = Interface(conn, 'gi2/0')
a = interface.get_interface_list()
from pprint import pprint
print(a)
# vlan = Vlan(conn,'150')
# print(vlan.get_vlan_list())


iface_config = {
    'admin': 'down',
    'description': 'configured by hpcmw7',
    'type': 'bridged',
}


l2_config = {
    'PVID': '100',
    'LinkType': '2',
}
# ret = interface.build(**iface_config)
# ret = interface.build(**l2_config)
# print(ret)
# print(interface.update())
# print(interface.get_config())

from lxml import etree
from lxml.builder import ElementMaker

str="""
<AntiVirus>
<Policies>
<Policy>
<PolicyName></PolicyName>
<Description></Description>
<CloudQuery></CloudQuery>
</Policy>
</Policies>
</AntiVirus>"""
