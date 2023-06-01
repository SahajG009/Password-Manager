#advance password manager
# using symmetric encryption
from cryptography.fernet import Fernet

#generating the key
#no need for key generation as we have it
'''def gen_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as kf:
        kf.write(key)'''

