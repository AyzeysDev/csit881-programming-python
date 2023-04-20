import hashlib
import time
def PermGen(char_set, max_len):
    if max_len <= 0:
        return
    for c in char_set:
        yield c
    for c in char_set:
        for next in PermGen(char_set, max_len-1):
            yield c + next
password = 'Az#$123'
hashNew = hashlib.sha1(password.encode()).hexdigest()

passwordHash = '447191b34890d34ff3a5b52473b2ff0f2028add4'

start = time.time()
result = PermGen('abcdefghijklmnopqrstuvwxyz#$%@A123', 7)

print(result)
# for item in list(result):
#     hashvalue = hashlib.sha1(item.encode()).hexdigest()
#     if(hashvalue == hashNew):
#         break
# end = time.time()
# print(end - start)