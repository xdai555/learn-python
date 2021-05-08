from pysnmp.hlapi import *


engine = SnmpEngine()
userData = UsmUserData(
    userName='admin',
    authKey='Admin@h3c',
    privKey='Admin@h3c',
    authProtocol=usmHMACMD5AuthProtocol,
    privProtocol=usmAesCfb128Protocol,
)
communityData = CommunityData('public')
target = UdpTransportTarget(('192.168.56.20',161))
context = ContextData()

def getSysName(target):
    sysname = ObjectIdentity("1.3.6.1.2.1.1.5.0")
    sysname1 = ObjectIdentity('SNMPv2-MIB','sysName',0)
    obj1 = ObjectType(sysname)
    g = getCmd(engine,userData,target,context,obj1)
    _,_,_,result = next(g)
    for i in result:
        print(i)


def getIfaceList(target):
    ifaceListOid = ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2'))
    g = nextCmd(engine,userData,target,context,ifaceListOid,lexicographicMode=False)
    try:
        while True:
            errorIndication, errorStatus, errorIndex, varBinds = next(g)
            for iface in varBinds:
                print(iface)
    except StopIteration:
        print('Get interface list done.')

getSysName(target)
getIfaceList(target)