#encoding:UTF-8
# -*- coding: utf-8 -*-

import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.0.185', port=22, username='wp', password='5620079')
stdin, stdout, stderr = ssh.exec_command("sudo fdisk -l")
data = stdout.read().splitlines()
for line in data:
    if line:
        print(line)
stdin.write('5620079\n')
stdin.flush()
data = stdout.read().splitlines()
for line in data:
    if line:
        print(line)
# 关闭连接
ssh.close()