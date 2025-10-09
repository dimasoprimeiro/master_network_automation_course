import paramiko
import time


def connect(server_ip, server_port, user, passwd):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to {server_ip}')
    ssh_client.connect(hostname=server_ip, port=server_port, username=user, password=passwd)
    return ssh_client
#função acima define o metodo de conexão nos equipamentos!

def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell
# a função acima inovoca o shel???? cria um shell object

def send_command(shell, command, timeout=1):
    print(f'Mandando o comando namoralzinha : {command}')
    shell.send(command + '\n')
    time.sleep(timeout)
# esta função define qual comando será enviado

def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode() #converter para string
#essa função retorna os comandos.

def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print('Fechando a porra da conexão!! AI PAI PARA!')
        ssh_client.close()
#essa função fecha a conexão


if __name__ == '__main__':
    router1 = {'server_ip': '192.168.0.162', 'server_port': '22', 'user': 'dimas', 'passwd': 'cisco'}
    client = connect(**router1)
    shell = get_shell(client)

    send_command(shell, 'enable' )
    send_command(shell, 'cisco' )
    send_command(shell, 'ter len 0' )
    send_command(shell, 'show version' )
    send_command(shell, 'sh ip int bri' )

    output = show(shell)
    print(output)

