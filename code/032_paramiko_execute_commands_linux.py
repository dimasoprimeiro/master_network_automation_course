import paramiko
import time


ssh_client = paramiko.SSHClient()

#conectando no equipamento

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())



linux = {
    'hostname': '192.168.0.203',
    'port': 22,
    'username': 'dimas',
    'password': 'Chinelosak47'
}
print(f'Conectando namoral no {linux['hostname']}')
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh_client.exec_command('ifconfig\n')
time.sleep(0.5)
output = stdout.read()
output = output.decode()
print(output)

stdin, stdout, stderr = ssh_client.exec_command('who24342e\n')
time.sleep(0.5)
output = stdout.read()
output = output.decode()
print(output)

print(stderr.read().decode())

#fechando conexão
if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()