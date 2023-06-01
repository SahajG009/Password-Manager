#advance password manager
# using symmetric encryption
from cryptography.fernet import Fernet

#generating the key
def gen_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as kf:
        kf.write(key)

gen_key()