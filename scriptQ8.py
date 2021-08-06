import sys
import hashlib
import uuid

salt = uuid.uuid4().hex
dk = hashlib.sha512(salt.encode() + sys.argv[1].encode()).hexdigest()
print(dk)