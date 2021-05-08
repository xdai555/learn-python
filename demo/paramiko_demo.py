import paramiko
from pprint import pprint
import re


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
ssh.connect(
    hostname='192.168.56.20',
    username='netdevops',
    password='netdevops',
    allow_agent=False,
    look_for_keys=False,
)
stdin, stdout,  stderr = ssh.exec_command('dis ip int brief')
interface = stdout.read()
print(stdout)
print(interface)
ssh.close()

# key = paramiko.RSAKey.from_private_key_file(r"C:\Users\xdai\.ssh\id_rsa")
# tran = paramiko.Transport("192.168.56.20", 22)
# tran.connect(username='admin', pkey=key)
# sftp = paramiko.SFTPClient.from_transport(tran)
# local_path = r"C:\11111"
# remote_path = r"id_rsa.pub"
# sftp.get(remotepath=remote_path, localpath=local_path)
# sftp.put(local_path,'/3333')
# sftp.close()
