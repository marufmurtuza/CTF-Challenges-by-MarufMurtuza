
secret = input("Enter your string to decrypt: ")

key = input("Enter the key: ")

secarr = []

keyarr = []

x = 0

def keyfunc(key,keyarr,x):

    for character in key:

        keyarr.append(ord(character))

    for i in keyarr:

        x += i


def secfunc(secret,secarr,key,x):

    for character in secret:

        secarr.append(ord(character))

    for i in range(len(secarr)):

        if 91 <= secarr[i] <= 122:

            secarr[i] = secarr[i] + 6

        else:

            if 54 <= secarr[i] <= 90:

                secarr[i] = secarr[i] + 11

    if len(key) % 2 ==0:

        x = x - 1

    else:

        x = x - 3

    if x % 2 == 0:

        secarr[i] = secarr[i] - 3

    else:

        secarr[i] = secarr[i] - 2 

    decrypted = ""

    for val in secarr:

        decrypted = decrypted + chr(val)

    print("Decrypted Text: " + decrypted)


keyfunc(key,keyarr,x)

secfunc(secret,secarr,key,x)
