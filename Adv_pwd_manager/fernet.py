#using fernet module

from cryptography.fernet import Fernet
#data encryption
#key should be safe
key = Fernet.generate_key()
f = Fernet(key)
print(key)
#message that needs to be encrypted should be in bytes not string
message = b'sahaj'
#encrypt the message
#result of this encryption is called Fernet Token
fernettoken = f.encrypt(message)
print(fernettoken)
#decrypt the message
decryptedmsg = f.decrypt(fernettoken)
print(decryptedmsg)
#converting from bytes to string
a = decryptedmsg.decode()
print(a)