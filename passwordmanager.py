from cryptography.fernet import Fernet as ff



'''def write_key():
  key = f.generate_key()
  with open("key.key", "wb") as key_file:
    key_file.write(key)

write_key()
'''

def loadkey():
  file =  open("key.key", "rb")
  key = file.read()
  file.close()
  return key


master_pwd = input('what is the master password') 
key  = loadkey() + master_pwd.encode()
fer = ff(key)

def view():
   with open('passwords.txt','r') as f:
    for line in f.readlines():
     data = line.rstrip()
     user, passw = data.split("|")
     print("User:", user , "Password:", fer.decrypt(passw.encode()).decode())



 
def add():
  name = input('account name:')
  pwd = input( 'password:')  
  
  with open('passwords.txt','a') as f:
    f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + "\n")
while True:
  mode = input('would like to add a new password or view existing ones (view)').lower()
  if mode == 'x':
   break

  if mode == 'view':
   view()
  elif mode == 'add':
    add()
  else:
    print('invalid')
