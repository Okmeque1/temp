import random
def generate():
    password = ''
    for x in range(3):
      password += random.choice('!"$£%$^&%$£T$(IEGDDVOG)E')
    print(password)
generate()
