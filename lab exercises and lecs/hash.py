import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend

# salt = os.urandom(16)
#
# kdf = Scrypt(salt=salt, length =32, n=2**14, r=8, p=1, backend=default_backend())
# key = kdf.derive(b'csit970*')
salt = b'\xe4ax\x96hx\xa6\xe4\x8b\xd3 \x19"\x7f\x9cC'
key = b'?]\xeeLXu\x06\x8f\xc4\xcc\xa8\x05\x95L\xff`\xe7\xb7\xb0\x19Z\x0f\xbf\xa0\xc0\xfb\x93\x03\xf3|\xdc'

pwd = input("Enter yur password here")

verifyKey = kdf.verify()

print("key: ", key)
print("salt: ", salt)