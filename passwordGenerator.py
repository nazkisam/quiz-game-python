import random as r
import string as str

def generate_password(min_length, numbers = True , special_characters = True):
  letters = str.ascii_letters
  digits = str.digits
  special = str.punctuation
 
  characters = letters
  if numbers:
    characters += digits
  if special:
    characters += special
  
  pwd = ''
  meets_criteria = False
  has_number = False
  has_special  = False
  
  while not meets_criteria and len(pwd) < min_length:
    newchar = r.choice(characters)
    pwd += newchar

    if newchar in digits:
      has_number = True
    elif newchar in special:
      has_special = True 
    
    meets_criteria = True 
    
    if numbers:
      meets_criteria = has_number
    if special_characters:
      meets_criteria = meets_criteria and has_special


  return pwd
      


leng = int(input('enter the number '))
has_number = input('press y to include numbers').lower() == 'y'
has_char = input('enter y to add character').lower() == 'y'
pwd = generate_password(leng, has_number, has_char)  
print (pwd)