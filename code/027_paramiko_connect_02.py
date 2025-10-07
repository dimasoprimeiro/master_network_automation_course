import paramiko

ssh_client = paramiko.SSHClient()

#conectando no equipamento

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# ssh_client.connect(hostname='192.168.0.114', port=22, username='cisco', password='cisco', look_for_keys=False, allow_agent=False)
# print(ssh_client.get_transport().is_active)

router = {
    'hostname': '192.168.0.114',
    'port': 22,
    'username': 'cisco',
    'password': 'cisco'
}
print(f'Connecting to {router['hostname']}')
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)


#fechando conexão
print('Closing connection')
ssh_client.close()