import paramiko
import time
import getpass

ssh_client = paramiko.SSHClient()

#conectando no equipamento

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

password = getpass.getpass('poe a senha ai seu animal: ')

linux = {
    'hostname': '192.168.0.203',
    'port': 22,
    'username': 'dimas',
    'password': password
}
print(f'Conectando namoral no {linux['hostname']}')
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

shell = ssh_client.invoke_shell()
shell.send('cat /etc/passwd\n')
time.sleep(1)

shell.send('sudo cat /etc/shadow\n')
shell.send('Chinelosak47\n')
time.sleep(1)




output = shell.recv(10000).decode()
print(output)

#fechando conexão
if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()