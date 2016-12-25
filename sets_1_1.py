#python 3
import base64, binascii

def challenge_1(string=b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'):
	#Binary data of hexadecimal representation
	#help(binascii.a2b_hex)
	cipher = binascii.unhexlify(string)

	print(cipher)
	# b"I'm killing your brain like a poisonous mushroom"

	#must be a binary
	type(cipher)

	answer = base64.b64encode(cipher)
	#SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

	return answer

a = challenge_1(b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
print(a)