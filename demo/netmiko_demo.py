from netmiko import ConnectHandler as ch
import ntc_templates
import os
from pprint import pprint


"""
Netmiko已配置为自动在〜/ntc-template/templates/index中查找ntc-templates索引文件。
另外，可以通过设置以下环境变量来明确告诉Netmiko在哪里寻找TextFSM模板目录（请注意，此目录中必须有一个索引文件）：
`export NET_TEXTFSM=/path/to/ntc-templates/templates/`
"""
# 配置环境变量
NET_TEXTFSM=ntc_templates.__file__
os.environ['NET_TEXTFSM'] = os.path.dirname(ntc_templates.__file__)


def exec_command(host, command,**kwargs):
    conn = ch(**host)
    output = conn.send_command(command, **kwargs)
    conn.disconnect()
    return output


def exec_command_timing(host, command, **kwargs):
    conn = ch(**host)
    output = conn.send_command_timing(command, **kwargs)
    conn.disconnect()
    return output

host = {
    'device_type': 'hp_comware',
    'host': '192.168.56.20',
    'username': 'netdevops',
    'password': 'netdevops',
    'port': 830,
}
# cmd = 'copy http://192.168.56.1:9212/vlan.cfg flash:/'
conn = ch(**host)
hello = """<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<capabilities> 
 <capability>urn:ietf:params:netconf:base:1.0</capability> 
 </capabilities> 
</hello>]]>]]>"""
close_session = """<rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"><close-session/></rpc>]]>]]>"""
conn.send_command('xml')
output = conn.send_command(hello)
print(output)

# output = conn.send_command(cmd, expect_string=r'\[Y/N\]:')
# output += conn.send_command('Y', expect_string=r'>')
# print(output)

def config_backup(host, diff):
    conn = ch(**host)
    running_config = conn.send_command("display current configuration")
    startup_config = conn.send_command("more flash:/startup.cfg")
    return 

"""配置备份，需要关注的点：
1. 运行时配置和启动配置，如何保存配置：文件、目录、日期、设备名称；涉及本地开启文件服务器的配置
2. 启动配置的保存路径（设备 put 到服务器上），这里还要注意，source 地址，vpn-instance 参数
3. 配置一致性比对：通过 difflab 来实现
"""