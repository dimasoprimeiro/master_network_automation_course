import myparamiko


router = {'server_ip': '192.168.0.162', 'server_port': '22', 'user': 'dimas', 'passwd': 'cisco'}
client = myparamiko.connect(**router)
shell = myparamiko.get_shell(client)


myparamiko.send_command(shell, 'ter len 0')
# myparamiko.send_command(shell, 'enable')
# myparamiko.send_command(shell, 'cisco')
myparamiko.send_command(shell, 'sh run\n')


output = myparamiko.show(shell)
# print(output)
output_list = output.splitlines()
output_list = output_list[16:-1]
# print(output_list)
output = '\n'.join(output_list)
# print(output)

from datetime import datetime
now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

file_name = f'{router['server_ip']}_{year}-{month}-{day}.txt'
print(file_name)

with open(file_name, 'w') as f:
    f.write(output)

myparamiko.close(client)
