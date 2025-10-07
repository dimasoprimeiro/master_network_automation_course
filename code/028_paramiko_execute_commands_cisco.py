import paramiko
import time

ssh_client = paramiko.SSHClient()

#conectando no equipamento

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

router = {
    'hostname': '192.168.0.114',
    'port': 22,
    'username': 'cisco',
    'password': 'cisco'
}
print(f'Connecting to {router['hostname']}')
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

#enviando e coletando comandos para o equipamento
shell = ssh_client.invoke_shell()# invoka o shell do equipamento

shell.send('ter len 0\n')
shell.send('show version\n')
shell.send('show ip int bri\n')
time.sleep(1)# dar tempo para o shell do equipamento

output = shell.recv(10000)
# print(type(output))
output = output.decode('utf-8') #mudar o tipo de dado
print(output)


#fechando conexão
if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()