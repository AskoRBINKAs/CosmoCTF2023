import hashlib
def split_pairs(line):
    n = 2
    new_list = []
    for i in range(0, len(line), n):
        element = line[i:i+n]
        if len(element) == 1:
            new_list.append(element + '_')
        else:
            new_list.append(element)
    
    return new_list
hash = input()
hash = hashlib.md5(hash.encode()).hexdigest()
if len(hash)!=32:
    exit(-1)
hash=split_pairs(hash)
flag=""
blocks=[]
for i in range(len(flag)):
    a = int("0x"+hash[i%16],16)
    b = int(flag[i])
    r = (a**b)
    blocks.append(r)
print(blocks)     