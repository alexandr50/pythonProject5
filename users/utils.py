import random
import string

def generate_code():
    random.seed()
    return str(random.randint(1000, 9999))

def generate_invite_code():

    symbols = string.ascii_letters + '0123456789'
    return ''.join(random.choice(symbols) for i in range(6))
