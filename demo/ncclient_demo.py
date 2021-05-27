from ncclient import manager
from lxml import etree
from lxml.builder import ElementMaker
from pprint import pprint
import logging
# logging.basicConfig(level=logging.DEBUG)


BASE_NS_1_0 = "urn:ietf:params:xml:ns:netconf:base:1.0"
H3C_BASE_1_0 = "http://www.h3c.com/netconf/base:1.0"
H3C_CONFIG_1_0 = "http://www.h3c.com/netconf/config:1.0"
H3C_DATA_1_0 = "http://www.h3c.com/netconf/data:1.0"
H3C_DATA_1_0_C = '{' + H3C_DATA_1_0 + '}'
H3C_ACTION_1_0 = "http://www.h3c.com/netconf/action:1.0"


get_bgp_asn_raw = """<rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <get>
        <filter type="subtree">
            <top xmlns="http://www.h3c.com/netconf/data:1.0">
                <BGP>
                    <Instances>
                        <Instance>
                            <Name></Name>
                            <ASNumber></ASNumber>
                        </Instance>
                    </Instances>
                </BGP>
            </top>
        </filter>
    </get>
</rpc>"""

# 实际使用时，对于 get 系列操作， filter 元素下的内容为 H3C 自有部分；
# 对于 edit-config 系列操作， config 元素下的内容为 H3C 自有部分；
# 自有部分默认情况下以 top 元素为起点。
get_bgp_asn = """<top xmlns="http://www.h3c.com/netconf/data:1.0">
    <BGP>
        <Instances>
            <Instance>
                <Name></Name>
                <ASNumber></ASNumber>
            </Instance>
        </Instances>
    </BGP>
</top>"""

get_all_iface = """
<top xmlns="http://www.h3c.com/netconf/data:1.0">
<Ifmgr>
<Interfaces>
<Interface>
<Name></Name>
<ifType></ifType>
<Description></Description>
<AdminStatus></AdminStatus>
<OperStatus></OperStatus>
<ConfigSpeed></ConfigSpeed>
<ActualSpeed></ActualSpeed>
<ConfigDuplex></ConfigDuplex>
<ActualDuplex></ActualDuplex>
<LinkType></LinkType>
<PVID></PVID>
<InetAddressIPV4></InetAddressIPV4>
<InetAddressIPV4Mask></InetAddressIPV4Mask>
<PhysicalIndex></PhysicalIndex>
<MAC></MAC>
<PortLayer></PortLayer>
<ForwardingAttributes></ForwardingAttributes>
<Loopback></Loopback>
<MDI></MDI>
<ConfigMTU></ConfigMTU>
<ActualMTU></ActualMTU>
<ConfigBandwidth></ConfigBandwidth>
<ActualBandwidth></ActualBandwidth>
</Interface>
</Interfaces>
</Ifmgr>
</top>
"""

host = {
    'host': '192.168.56.20',
    'username': 'netdevops',
    'password': 'netdevops',
    'port': 830,
    'device_params': {'name': 'h3c'},

}

E = ElementMaker(namespace=H3C_DATA_1_0, nsmap={None: H3C_DATA_1_0})
top = E.top(
    E.Ifmgr(
        E.Interfaces(
            E.Interface(
                E.Name(),
                E.InetAddressIPV4(),
                E.AdminStatus()
            )
        )
    )
)
# print(dir(top))
# print(top.tag)
# print(etree.tostring(top))

conn = manager.connect(**host, hostkey_verify=False, look_for_keys=False)
# # 配置 BGP 111
# ret = conn.edit_config(target='running',config=hello)
# # 获取 BGP AS 号
# ret = conn.get(('subtree',get_bgp_asn))
# print(ret,type(ret),ret.data_ele.find('.//{http://www.h3c.com/netconf/data:1.0}ASNumber').text)

# 获取设备所有接口的所有信息
ret = conn.get(('subtree', top))
# print(ret,type(ret))
# print(dir(ret))
# print(ret.data,type(ret.data))

ipv4_xml="""
<IPV4ADDRESS>
 <Ipv4Addresses>
 <Ipv4Address>
 <IfIndex></IfIndex>
 <Ipv4Address></Ipv4Address>
 <Ipv4Mask></Ipv4Mask>
 <AddressOrigin></AddressOrigin>
 </Ipv4Address>
 </Ipv4Addresses>
</IPV4ADDRESS>"""

C = ElementMaker(namespace=BASE_NS_1_0, nsmap={None: BASE_NS_1_0})
E = ElementMaker(namespace=H3C_CONFIG_1_0, nsmap={None: H3C_CONFIG_1_0})
xml_ifcfg = C.config(
    E.top(
        E.IPV4ADDRESS(
            E.Ipv4Addresses(
                E.Ipv4Address(
                    E.IfIndex("2"),
                    E.Ipv4Address("1.1.1.1"),
                    E.Ipv4Mask("255.255.255.0")
                )
            )
        )
    )
)

# print(etree.tostring(xml_ifcfg))

# ret = conn.edit_config(target="running", config=xml_ifcfg)
# print(ret)

xml_bgp_asn_cfg = """<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <top xmlns="http://www.h3c.com/netconf/config:1.0">
<BGP>
 <Instances>
 <Instance>
 <Name></Name>
 <ASNumber>62333</ASNumber>
 </Instance>
 </Instances>
</BGP>
</top>
</config>"""
xml_bgp_familys_cfg="""<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<top xmlns="http://www.h3c.com/netconf/config:1.0">
<BGP>
<Familys>
<Family>
<Name></Name>
<VRF></VRF>
<Type>1</Type>
</Family>
</Familys>
</BGP>
</top>
</config>
"""
xml_bgp_net_cfg = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<top xmlns="http://www.h3c.com/netconf/config:1.0">
<BGP>
 <Networks>
 <Network>
 <Name></Name>
 <VRF></VRF>
 <Family>1</Family>
 <IpAddress>1.1.1.1</IpAddress>
 <Mask>24</Mask>
 </Network>
 </Networks>
</BGP>
</top>
</config>
"""

# ret = conn.edit_config(target="running", config=xml_bgp_asn_cfg)
# ret = conn.edit_config(target="running", config=xml_bgp_familys_cfg)
# ret = conn.edit_config(target="running", config=xml_bgp_net_cfg)
# print(ret)

# print(conn.connected)
# for c in conn.server_capabilities:
#     print(c)
# from pyhpecw7.comware import HPCOM7
# from pyhpecw7.features.interface import Interface
# conn = HPCOM7(**host)
# conn.open()

# interface = Interface(conn, 'gi0/2')
# iface_config = {
#     'admin': 'down',
#     'description': 'configured by hpcmw7',
# }
# interface.build(iface_config)
# interface.update()
# interface.get_config()


def elem_to_dict(elem, ns, key_map, value_map):
    to_dict = {}
    for k, v in key_map.items():
        field = elem.find('.//{}{}'.format(ns, v))
        if field is not None:
            text = field.text
            # to_dict[k] = value_map.get(v, {}).get(text, text)
            to_dict[k] = text
    return to_dict

def elem_to_dict_raw(elem, ns):
    to_dict = {}
    for e in elem.getchildren():
        to_dict[e.tag.replace(ns,'')] = e.text
    return to_dict



def data_elem_to_dict(elem, key_map, value_map={}):
    return elem_to_dict(elem, H3C_DATA_1_0_C, key_map, value_map=value_map)



iface_key_map = {
    '接口名称': 'Name',
    'MTU': 'ActualMTU',
    'IP 地址': 'InetAddressIPV4',
    '掩码': 'InetAddressIPV4Mask',
}

result = data_elem_to_dict(ret.data,iface_key_map)

def find_all_in_data(elem, v):
    return _findall(elem, H3C_DATA_1_0_C, v)


def _findall(elem, ns, v):
    return elem.findall('.//{}{}'.format(ns, v))


ifaces = find_all_in_data(ret.data_ele,'Interface')
# print(ifaces)
# print(etree.tostring(ifaces[0]))

# for i in ifaces[0]:
#     print(i.tag, i.text)

result = [elem_to_dict_raw(iface, H3C_DATA_1_0_C) for iface in ifaces]
result = [data_elem_to_dict(iface,iface_key_map) for iface in ifaces]

# print(result)
import xmltodict
# print(dir(xmltodict))
result = xmltodict.parse(etree.tostring(ifaces[0]))
print(result)
print(dict(result['Interface']))