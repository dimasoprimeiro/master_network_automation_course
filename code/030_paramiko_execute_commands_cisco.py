import paramiko
import time
import getpass

ssh_client = paramiko.SSHClient()

#conectando no equipamento

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

password = getpass.getpass('poe a senha ai seu animal: ')

router1 = {
    'hostname': '192.168.0.159',
    'port': 22,
    'username': 'cisco',
    'password': password
}

router2 = {
    'hostname': '192.168.0.114',
    'port': 22,
    'username': 'cisco',
    'password': password
}

router3 = {
    'hostname': '192.168.0.220',
    'port': 22,
    'username': 'cisco',
    'password': password
}

routers = [router1, router2, router3]

for router in routers:

    print(f'Connecting to {router['hostname']}')
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

    #enviando e coletando comandos para o equipamento
    shell = ssh_client.invoke_shell()# invoka o shell do equipamento


    shell.send('conf t\n')
    shell.send('router ospf 1 \n')
    shell.send('network 0.0.0.0 0.0.0.0 area 0\n')
    shell.send('end\n')
    shell.send('ter len 0\n')
    shell.send('sh ip protocols\n')
    time.sleep(2)# dar tempo para o shell do equipamento

    output = shell.recv(10000).decode()
    print(output)


#fechando conexão
if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()