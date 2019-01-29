#encoding:UTF-8
# -*- coding: utf-8 -*-
import paramiko

import getpass



# create ssh connection
key_filename = 'id_rsa'
try:
    key = paramiko.RSAKey.from_private_key_file(key_filename)
except paramiko.PasswordRequiredException:
    password = getpass.getpass('RSA key password: ')
    pkey = paramiko.RSAKey.from_private_key_file(key_filename, password)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.0.185', username='wp', compress=True, pkey=key)
# 执行命令
stdin, stdout, stderr = ssh.exec_command('df -hl')
# 结果放到stdout中，如果有错误将放到stderr中
print(stdout.read().decode())
ssh.close()
