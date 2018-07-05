import ftplib
import os

def online():
  try:
    username = os.environ.get('USERNAME', None)
    password = os.environ.get('PASSWORD', None)
    ftp = ftplib.FTP()
    ftp.connect("ftp.ezyro.com", 21)
    ftp.login(username, password)
    #ftp.cwd("htdocs")
    #ftp.cwd("arquivos")
    ftp.quit()
    return True
  except:
    return False
  
def salvar(nome_arquivo):
  try:
    username = os.environ.get('USERNAME', None)
    password = os.environ.get('PASSWORD', None)
    ip = os.environ.get('IP', None))
    ftp = ftplib.FTP()
    ftp.connect("ftp.ezyro.com", 21)
    ftp.login(username, password)
    ftp.pwd()
    ftp.cwd("htdocs")
    ftp.cwd("arquivos")
    try:
      ftp.delete(nome_arquivo)
    except:
      pass
    ftp.storbinary('STOR {}'.format(nome_arquivo), open(nome_arquivo,'rb'))
    
  except:
    ftp.pwd()
    ftp.cwd("htdowcs")
    ftp.cwd("arquivos")
    try:
      ftp.delete(nome_arquivo)
    except:
      pass
    ftp.storbinary('STOR {}'.format(nome_arquivo), open(nome_arquivo,'rb'))
    
