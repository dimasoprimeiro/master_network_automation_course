import myparamiko
client = myparamiko.connect('192.168.0.203', '22', 'dimas', 'Chinelosak47')
shell = myparamiko.get_shell(client)
myparamiko.send_command(shell, 'uname -a')

cmd = 'sudo groupadd developers'
myparamiko.send_command(shell, cmd)
myparamiko.send_command(shell, 'Chinelosak47', 2)
myparamiko.show(shell)
myparamiko.send_command(shell, 'tail -n 1 /etc/group')


output = myparamiko.show(shell)

print(output)

myparamiko.close(client)