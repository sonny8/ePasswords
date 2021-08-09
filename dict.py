print("Welcome to ePasswords, Emerson!")
def main():
    print("Enter the name of the password: ")
    name = input("")

    w = open(name, "w")

    print('Enter the password(Do not include a ".") : ')

    passw = input("")



    print("Creating password entry...")
    w.write(passw+'.txt')
    w.close()
    print("done!")










