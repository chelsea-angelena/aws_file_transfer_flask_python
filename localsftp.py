import pysftp

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
# change these and set as secret (these are just generic values currently)
host="127.0.0.1"
username="sftp_user"
password="SFTPUSERPASSWORDHERE"
port=32768

def get_sftp():
    return pysftp.Connection(host, username=username, password=password, cnopts=cnopts, port=port)

