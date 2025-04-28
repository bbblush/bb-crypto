import base64
Running = True
strength = 8
print("Welcome to bb-crypto! Choose a function!")
while Running:
    print("1 - encrypt text using bb-method")
    print("2 - decrypt text using bb-method")
    print("3 - encryption settings")
    print("4 - exit")
    v = int(input())
    if v == 1:
        print('Enter the encryption key (number 0-255)')
        tkey = int(input())
        print("Do you want to load text from a file? Y/N (the file must be named text.txt and be in the program's working directory)")
        s = input()
        if s == 'Y' or s == 'y':
            with open("text.txt", "r", encoding="utf-8") as file:
                txt = file.read()
            print('The text was loaded from text.txt in the program\'s working directory.')
        else:
            print('Enter the text to encrypt:')
            txt = input()
        txtb = txt.encode('utf-8')
        bkey = bin(tkey)[2:]
        bkeys = str(bkey)
        bkeys = ('0' * (strength - len(bkeys))) + bkeys
        for i in range(strength):
            if bkeys[i] == '1':
                txtb = base64.b64encode(txtb)
                print("Encrypting. Cycle: ", i, "/", strength)
            elif bkeys[i] == '0':
                txtb = base64.b32encode(txtb)
                print("Encrypting. Cycle: ", i, "/", strength)
        txt = txtb.decode('utf-8')
        print('Done, your ciphertext: ', txt)
        print("Do you want to save the ciphertext to a file? Y/N")
        s = input()
        if s == 'Y' or s == 'y':
            with open("crypto.txt", "w", encoding="utf-8") as file:
                file.write(txt)
            print('The ciphertext was saved to crypto.txt in the program\'s working directory.')
        print('='*50)
    elif v == 2:
        print('Enter the decryption key (number 0-255)')
        tkey = int(input())
        print("Do you want to load the ciphertext from a file? Y/N (the file must be named crypto.txt and be in the program's working directory)")
        s = input()
        if s == 'Y' or s == 'y':
            with open("crypto.txt", "r", encoding="utf-8") as file:
                txt = file.read()
            print('The ciphertext was loaded from crypto.txt in the program\'s working directory.')
        else:
            print('Enter the text to decrypt:')
            txt = input()
        txtb = txt.encode('utf-8')
        bkey = bin(tkey)[2:]
        bkeys = str(bkey)
        bkeys = ('0' * (strength - len(bkeys))) + bkeys
        for i in range(strength):
            if bkeys[((strength-1)-i)] == '1':
                txtb = base64.b64decode(txtb)
                print("Decrypting. Cycle: ", i, "/", strength)
            elif bkeys[((strength-1)-i)] == '0':
                txtb = base64.b32decode(txtb)
                print("Decrypting. Cycle: ", i, "/", strength)
        txt = txtb.decode('utf-8')
        print('Done, your decrypted text: ', txt)
        print("Do you want to save the decrypted text to a file? Y/N")
        s = input()
        if s == 'Y' or s == 'y':
            with open("text.txt", "w", encoding="utf-8") as file:
                file.write(txt)
            print('The decrypted text was saved to text.txt in the program\'s working directory.')
        print('='*50)
    elif v == 3:
        print('Enter the encryption strength, currently set to', strength)
        print('Best options: 2/4/8/16/32/64 (the higher the number, the longer the ciphertext, but more secure)')
        strength = int(input())
        print("Done, strength set to", strength)
        print('='*50)
    elif v == 4:
        Running = False