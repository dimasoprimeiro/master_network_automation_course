import paramiko

ssh_client = paramiko.SSHClient()

#conectando no equipamento
print('Connecting to device')
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname='192.168.0.114', port=22, username='cisco', password='cisco', look_for_keys=False, allow_agent=False)
print(ssh_client.get_transport().is_active)





#fechando conexão
print('Closing connection')
ssh_client.close()