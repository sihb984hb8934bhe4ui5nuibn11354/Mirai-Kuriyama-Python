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
    
def baixar(nome_arquivo_1, nome_saida):
  try:
    username = os.environ.get('USERNAME', None)
    password = os.environ.get('PASSWORD', None)
    ftp = ftplib.FTP()
    ftp.connect("ftp.ezyro.com", 21)
    ftp.login(username, password)
    ftp.pwd()
    ftp.cwd("htdocs")
    ftp.cwd("arquivos")
    ftp.retrbinary("RETR " + nome_arquivo_1 ,open(nome_saida, 'wb').write)
  except:
    ftp.pwd()
    ftp.cwd("htdowcs")
    ftp.cwd("arquivos")
    ftp.retrbinary("RETR " + nome_arquivo_1 ,open(nome_saida, 'wb').write)

def baixar_valor(nome_arquivo_1):
  try:
    username = os.environ.get('USERNAME', None)
    password = os.environ.get('PASSWORD', None)
    ftp = ftplib.FTP()
    ftp.connect("ftp.ezyro.com", 21)
    ftp.login(username, password)
    ftp.pwd()
    ftp.cwd("htdocs")
    ftp.cwd("arquivos")
    ftp.retrbinary("RETR " + nome_arquivo_1 ,open(nome_arquivo_1, 'wb').write)
    file = open(nome_arquivo_1, "rb").read()
    os.remove(nome_arquivo_1)
    return file
  except:
    ftp.pwd()
    ftp.cwd("htdowcs")
    ftp.cwd("arquivos")
    ftp.retrbinary("RETR " + nome_arquivo_1 ,open(nome_arquivo_1, 'wb').write)
    file = open(nome_arquivo_1, "rb").read()
    os.remove(nome_arquivo_1)
    return file
    
def criar_arquivo(nome_arquivo_2, valor_f):
  file = open(nome_arquivo_2, "wb")
  file.write(valor_f)
  file.close()
    
    
