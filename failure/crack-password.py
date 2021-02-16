import tenacity
from random import randint

# Dummy 2 digit password
password = randint(10, 99) 

print("Password:", password)

def crackPassworrd():
    to_check = randint(10, 99)
    if password != to_check:
        print("No luck yet with: ", to_check)
        raise RuntimeError
    print("Password Cracked!!! - ", to_check)

#### Write code below this line
@tenacity.retry(wait=tenacity.wait_fixed(1))
def runCrackPassword():
    crackPassworrd()

runCrackPassword()