import winrm
import paramiko


# winrm = windows remote machines
# winrm used to give a command on any remote machine.
# 19@@
# session = winrm.Session()
port = winrm.protocol.Protocol(endpoint="http://server:5985/wsman",
                               transport="ntlm",
                               username="ravit",
                               password="ravitE!2",
                               server_cert_validation="ignore")

shell = port.open_shell()

command = port.run_command(shell,"ping www.google.com")

out, err, status = port.get_command_output(shell,command)

import winrm

host = 'YourWindowsHost'
domain = 'YourDomain'
user = 'YourDomainUser'
password = 'YourPassword'

session = winrm.Session(host, auth=('{}@{}'.format(user,domain), password), transport='ntlm')

result = session.run_cmd('ipconfig', ['/all']) # To run command in cmd

