import ftplib
import os

def conectar():
  username = str(os.environ.get('USERNAME', None))
  password = str(os.environ.get('PASSWORD', None))
  ip = str(os.environ.get('IP', None))
  port = os.environ.get('PORT', None)
  ftp = ftplib.FTP()

  ftp.connect(ip, port)
  ftp.login(username, password)
  ftp.cwd("htdocs")
  ftp.cwd("arquivos")
