# first we need to import paramiko module because paramiko is third party library in python
import paramiko

# paramiko creates by sshclient
ssh = paramiko.SSHClient()

# Here we need to ask yes or no confirmation for connecting remote server at the first time or
# it is add as known host to on our local server
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# For connecting remote server we need to give username, hostname, password, port
ssh.connect(hostname="", username="", password="", port=22)

# Here we will be mention
local_path = ""

transferred_path = ""

# for copying and transferring files we need to create sftp client from ssh client,
# with this we will be open sftp client
sftp_client = ssh.open_sftp()

# here we will be copying files
sftp_client.get(local_path, transferred_path)

# once it done we need to close sftp client
sftp_client.close()

# once it done we need to close ssh client
ssh.close()
