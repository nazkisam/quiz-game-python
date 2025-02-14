master_pwd = input('what is the master password')




def view():
   with open('passwords.txt','r') as f:
    for line in f.readlines():
     print(line.rstrip())


 
def add():
  name = input('account name:')
  pwd = input( 'password:')  
  
  with open('passwords.txt','a') as f:
    f.write(name + '|' + pwd + "\n")
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
