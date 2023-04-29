charset = dict()
def gen_test():
    global charset
    with open("chars.txt") as flag_file:
        flag = flag_file.read().replace('\n','')

    modulo = 256
    public_key = 17

    flag_encrypted = []
    for c in flag:
        char_code = ord(c) * 2 - 1
        encrypted_char_code = pow(char_code, public_key, modulo)
        flag_encrypted.append(encrypted_char_code)

    #with open("rsa.enc", "wb") as encrypted_file:
     #   encrypted_file.write(bytes(flag_encrypted))
    for i in range(len(flag)):
        charset[flag_encrypted[i]]=flag[i]
    return (flag_encrypted)

char_array = gen_test()
flag_enc = None
with open("rsa.enc",'rb+') as f:
    flag_enc = f.read()
founded=[]
for i in flag_enc:
    if i in char_array:
        founded.append(i)
for i in founded:
    print(charset[i],end='')