import sys
import hashlib
import uuid

salt = uuid.uuid4().hex
dk = hashlib.pbkdf2_hmac('sha512', sys.argv[1].encode(), salt.encode(), 200000)
print(dk.hex())