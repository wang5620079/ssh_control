#encoding:UTF-8
# -*- coding: utf-8 -*-

import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.0.185', port=22, username='wp', password='5620079')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('df -hl')
# 结果放到stdout中，如果有错误将放到stderr中
print(stdout.read().decode())
# 关闭连接
ssh.close()