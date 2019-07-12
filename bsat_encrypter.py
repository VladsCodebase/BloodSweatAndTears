#!/usr/bin/env python

flag = 'Flag for Indonesia: ' + # Flag here

chars = [ord(character) for character in flag.upper()]

passphrase = # Corporate Key here
passcode = [ord(char) for char in passphrase.upper()]

encrypted_chars = []

count = 0
for char in chars:
	encrypted_chars.append(char * passcode[count % len(passphrase)])
	count += 1

with open('ciphertext.txt','w') as outfile:
	outfile.write(str(encrypted_chars))