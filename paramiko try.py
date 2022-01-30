import paramiko
import unittest
import subprocess
from datetime import datetime
import time

# Contants and varaiables
PING_COMMAND = "ping %s -c1"
TWO_SECONDS_DELAY = 2


class TestRemoteExec():
    """Execute shell commands remotely over SSH"""
    def __init__(self, username, password, remoteIp):
        self.username = username
        self.password = password
        self.ipAddress = remoteIp
        self.port = 22
        try:
            self.client = paramiko.client.SSHClient()
            self.client.load_system_host_keys()
            self.client.connect(self.ipAddress, self.port, self.username, self.password)
        except Exception as e:
            print("FAIL: {0} : {1}".format(datetime.now(), e))

remote_obj = TestRemoteExec("127.0.0.1","ravit","ravitejA!19")