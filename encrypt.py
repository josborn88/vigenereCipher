alphabet_pos = {'A':0, 'a':0, 'B':1, 'b':1, 'C':2, 'c':2, 'D':3, 'd':3,
'E':4, 'e':4, 'F':5, 'f':5, 'G':6, 'g':6, 'H':7, 'h':7, 'I':8, 'i':8,
'J':9, 'j':9, 'K':10, 'k':10, 'L':11, 'l':11, 'M':12, 'm':12, 'N': 13,
'n':13, 'O':14, 'o':14, 'P':15, 'p':15, 'Q':16, 'q':16, 'R':17, 'r':17,
'S':18, 's':18, 'T':19, 't':19, 'U':20, 'u':20, 'V':21, 'v':21, 'W':22,
'w':22, 'X':23, 'x':23, 'Y':24, 'y':24, 'Z':25, 'z':25 }


def encrypt(plain, shift):
	cipherText = ''
	for i in range(0, len(plain)):
		letterChange = ord(plain[i]) + alphabet_pos.get(shift[i])
		if letterChange > ord('Z'):
			letterChange -= 26
		letter = chr(letterChange)
		cipherText += letter

	return(cipherText)

def decrypt(cipher, shift):
	plaintext = ''
	for i in range(0, len(cipher)):
		letterChange = ord(cipher[i]) - alphabet_pos.get(shift[i])
		if letterChange < ord('A'):
			letterChange += 26
		letter = chr(letterChange)
		plaintext += letter
	return(plaintext)
while True:
        message = input('What is your message?')
        toEncrypt = message.replace(' ', '').upper()

        keys = input('what is your cipher key?').upper()

        operate = input('encrypt or decrypt?')
        if operate.lower() == 'e' or operate.lower() == 'encrypt':
                print(encrypt(toEncrypt, keys))

        elif operate.lower() == 'd' or operate.lower() == 'decrypt':
                print(decrypt(toEncrypt, keys))

 
#print(encrypt(toEncrypt, keys))
#print(decrypt((encrypt(toEncrypt, keys)),keys))

