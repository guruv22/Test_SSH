#!/usr/bin/python

import getpass

from sshcmdexec import SshCmdExec

sess = SshCmdExec()
hostname = input('hostname: ')
username = input('username: ')
password = getpass.getpass('password: ')
sess.login(hostname, username, password)
