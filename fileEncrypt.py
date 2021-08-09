from cryptography.fernet import Fernet as fnt
print("Welcome to epass-enc")
def encrypt():
    command = input("Enter the password name: ")
    key = fnt.generate_key()



    with open('mykey.key', 'wb') as mykey:
        mykey.write(key)

    print(key)


    f = fnt(key)

    with open(command, "rb") as original_file:
        original = original_file.read()
        print(original)

    enc = f.encrypt(original)
    command = input("Enter the file to write to: ")
    with open(command+'.txt', 'wb') as encfl:
        encfl.write(enc)


    print("Done.")
