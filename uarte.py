import random
def generate():
    password = ''
    for x in range(3):
      password += random.choice('!"$£%$^&%$£T$(IEGDDVOG)E')
    print(password)#if you do this for some reason CodeQL is pissed because the variable is called 'password', even though this is not a password generator
    
generate()


password = 'hello'
print(password)#test number 2
